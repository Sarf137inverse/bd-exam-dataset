# Conventions

## Abbreviations

### Exam
| Full | Code |
|------|------|
| board | b |
| admission | adm |

### Board
| Full | Code |
|------|------|
| dhaka | dka |
| chittagong | ctg |
| rajshahi | raj |
| sylhet | syl |
| cumilla | cum |
| jashore | jas |
| barisal | bar |
| dinajpur | din |
| mymensingh | myn |
| madrasah | mad |
| technical | tec |

### Category (admission only)
| Full | Code |
|------|------|
| engineering | eng |
| university | uni |
| medical | med |

### Institution (admission only)
| Full | Code |
|------|------|
| buet | buet |
| cuet | cuet |
| ruet | ruet |
| kuet | kuet |
| dhaka university | du |
| chittagong university | cu |
| jahangirnagar university | ju |
| medical | med |

### Stage
| Full | Code |
|------|------|
| preliminary | pre |
| main | mn |

### Subject
| Full | Code |
|------|------|
| higher math 1st paper | m1 |
| higher math 2nd paper | m2 |
| physics 1st paper | p1 |
| physics 2nd paper | p2 |
| chemistry 1st paper | c1 |
| chemistry 2nd paper | c2 |
| biology 1st paper | b1 |
| biology 2nd paper | b2 |

---

## File ID Formula

```
# Board
b-{board}-{year}-{subject}
b-dka-2025-m1

# Admission with stage
adm-{institution}-{stage}-{year}-{subject}
adm-buet-pre-2019-m1

# Admission without stage
adm-{institution}-{year}-{subject}
adm-med-2020-b1
```

---

## Question ID Formula

```
{file_id}-{type}-{seq padded to 3}

b-dka-2025-m1-mcq-001
b-dka-2025-m1-cq-003
adm-buet-pre-2019-m1-mcq-047
```

---

## Stem Group ID Formula

```
{file_id}-mcq-sg-{seq padded to 2}

b-dka-2025-m1-mcq-sg-01
```

---

## Asset Filename Formula

```
{question_id}.png

b-dka-2025-m1-mcq-013.png
b-dka-2025-m1-mcq-sg-01.png
```

---

## Math Notation

- All math must be wrapped in $...$ for inline LaTeX
- Backslashes must be double-escaped: \\frac not \frac
- Bengali text stays as Bengali, no translation