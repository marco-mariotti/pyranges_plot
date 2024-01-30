import pyranges as pr
import pandas as pd


def get_introns(p):
    """Calculate introns df from a PyRanges object."""

    if "Feature" in p.columns:
        introns = p.df[p.df["Feature"] == "exon"]
    else:
        introns = p.df

    # intron start is exon end shifted
    introns["End"] = introns.groupby("transcript_id")["End"].shift()
    introns.dropna(inplace=True)
    # intron end is exon start
    introns.rename(columns={"Start": "End", "End": "Start"}, inplace=True)
    introns["Feature"] = ["intron"] * len(introns)

    return pr.from_dict(introns.to_dict())


def introns_shrink(df, ts_data, fil_data, thresh=0):
    """Calculate intron resizes and provide info for plotting"""

    chrom = df["Chromosome"].iloc[0]
    p = pr.from_dict(df.to_dict())

    # Calculate shrinkable intron ranges
    # get flexible introns
    p = p.sort(by=["transcript_id", "Start"])
    introns = get_introns(p)
    exons = p[p.Feature == "exon"]
    flex_introns = introns.subtract(exons)

    # get coordinate shift (delta) and cumulative coordinate shift (cumdelta)
    to_shrink = flex_introns.merge(strand=False)  # unique ranges
    to_shrink = to_shrink[to_shrink.End - to_shrink.Start > thresh]  # filtered
    to_shrink.delta = (
        to_shrink.df["End"] - to_shrink.df["Start"]
    ) - thresh  # calculate coord shift considering margins
    assert to_shrink.df.sort_values("Start").equals(
        to_shrink.df
    ), "PyRanges not sorted."
    to_shrink.cumdelta = to_shrink.df["delta"].cumsum()

    # store to shrink data
    ts_data[chrom] = to_shrink.df

    # Calculate exons coordinate shift
    exons = pd.concat([exons.df, to_shrink.df])
    exons.sort_values("Start", inplace=True)
    exons = exons.fillna({"cumdelta": 0})
    exons["cumdelta"] = exons["cumdelta"].replace(0, method="ffill")
    # match exons with its cumdelta
    exons = pr.from_dict(exons[exons["Feature"] == "exon"].to_dict())

    # Calculate fixed intron lines (FILs) and store in dictionary
    inters = introns.intersect(exons, strandedness=False).df
    inters["Feature"] = ["FIL"] * len(inters)
    fils = pd.concat([inters, to_shrink.df])
    fils.sort_values("Start", inplace=True)
    fils = fils.fillna({"cumdelta": 0})
    fils["cumdelta"] = fils["cumdelta"].replace(0, method="ffill")
    fils = fils[fils["Feature"] == "FIL"]
    fils["Start_adj"] = fils["Start"] - fils["cumdelta"]
    fils["End_adj"] = fils["End"] - fils["cumdelta"]
    fil_data[chrom] = fils

    # Adjust coordinates
    result = exons.df
    result["Start_adj"] = result["Start"] - result["cumdelta"]
    result["End_adj"] = result["End"] - result["cumdelta"]

    # Provide result
    return result[list(p.columns) + ["Start_adj", "End_adj", "cumdelta", "delta"]]
