import pyranges as pr


p1 = pr.PyRanges(
    {
        "Chromosome": [1, 1, 2, 2, 2, 2, 2, 3],
        "Strand": ["+", "+", "-", "-", "+", "+", "+", "+"],
        "Start": [1, 40, 10, 70, 85, 110, 150, 140],
        "End": [11, 60, 25, 80, 100, 115, 180, 152],
        "transcript_id": ["t1", "t1", "t2", "t2", "t3", "t3", "t3", "t4"],
        "feature1": ["a", "a", "b", "b", "c", "c", "c", "d"],
        "feature2": ["A", "A", "B", "B", "C", "C", "C", "D"],
    }
)

p2 = pr.PyRanges(
    {
        "Chromosome": [1, 1, 2, 2, 2, 2, 2, 3, 4, 4, 4, 4, 4, 4],
        "Strand": [
            "+",
            "+",
            "-",
            "-",
            "+",
            "+",
            "+",
            "+",
            "-",
            "-",
            "-",
            "-",
            "+",
            "+",
        ],
        "Start": [
            1,
            40,
            10,
            70,
            85,
            110,
            150,
            140,
            30100,
            30150,
            30500,
            30647,
            29850,
            29970,
        ],
        "End": [
            11,
            60,
            25,
            80,
            100,
            115,
            180,
            152,
            30300,
            30300,
            30700,
            30700,
            29900,
            30000,
        ],
        "transcript_id": [
            "t1",
            "t1",
            "t2",
            "t2",
            "t3",
            "t3",
            "t3",
            "t4",
            "t5",
            "t5",
            "t5",
            "t5",
            "t6",
            "t6",
        ],
        "feature1": [
            "1",
            "1",
            "1",
            "1",
            "1",
            "2",
            "2",
            "2",
            "2",
            "2",
            "2",
            "2",
            "2",
            "2",
        ],
        "feature2": [
            "A",
            "A",
            "B",
            "B",
            "C",
            "C",
            "C",
            "D",
            "E",
            "E",
            "E",
            "E",
            "F",
            "F",
        ],
        "Feature": [
            "exon",
            "exon",
            "CDS",
            "CDS",
            "CDS",
            "CDS",
            "CDS",
            "exon",
            "exon",
            "CDS",
            "CDS",
            "exon",
            "CDS",
            "CDS",
        ],
    }
)

p3 = pr.PyRanges(
    {
        "Chromosome": ["1"] * 10 + ["2"] * 10,
        "Strand": ["+", "+", "+", "+", "-", "-", "-", "-", "+", "+"]
        + ["+", "+", "+", "+", "-", "-", "-", "-", "+", "+"],
        "Start": [90, 61, 104, 228, 9, 142, 52, 149, 218, 151]
        + [6, 27, 37, 47, 1, 7, 42, 37, 60, 80],
        "End": [92, 64, 113, 229, 12, 147, 57, 155, 224, 153]
        + [8, 32, 40, 50, 5, 10, 46, 40, 70, 90],
        "transcript_id": ["t1", "t1", "t1", "t1", "t2", "t2", "t2", "t2", "t3", "t3"]
        + ["t4", "t4", "t4", "t4", "t5", "t5", "t5", "t5", "t6", "t6"],
    }
)


p_ala = pr.PyRanges(
    {
        "Start": [10, 50, 90] + [13, 60, 72, 120],
        "End": [20, 75, 130] + [16, 63, 75, 123],
        "Chromosome": [1] * 7,
        "id": ["gene1"] * 7,
        "trait1": ["exon"] * 3 + ["aa"] * 4,
        "trait2": ["gene_1"] * 3 + ["Ala"] * 4,
        "depth": [0] * 3 + [1] * 4,
    }
)

p_cys = pr.PyRanges(
    {
        "Start": [10, 50, 90] + [15, 55, 62, 100, 110],
        "End": [20, 75, 130] + [18, 58, 65, 103, 113],
        "Chromosome": [1] * 8,
        "id": ["gene1"] * 8,
        "trait1": ["exon"] * 3 + ["aa"] * 5,
        "trait2": ["gene_1"] * 3 + ["Cys"] * 5,
        "depth": [0] * 3 + [1] * 5,
    }
)
