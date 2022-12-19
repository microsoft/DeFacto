# DeFacto

## Introduction

DeFacto is a dataset containing human demonstrations and feedback for improving factual consistency of text summarization.

The dataset is constructed with the following steps:

1. **Detect errors**: The annotator is required to
evaluate a summary given the source document and
**decide if the summary is factually consistent**.
2. **Categorize errors**: If the annotator decides
the summary *is not* factually consistent, they are
required to **categorize the factual errors** in the
summary as either *intrinsic* or *extrinsic*.
3. **Give explanation**: The annotator is required to
**provide a natural language explanation** on why
the summary is factually consistent or not.
4. **Provide evidence**: The annotator is required to
*select a sentence from the source document as
evidence* to support their claims described in 3.
5. **Write corrective instruction**: The annotator is
required to **provide instructions** of how to correct
the original summary if they think it is not factually
consistent. To enforce uniformity and reduce the
noise in the instructions, we provide six templates
for the annotators corresponding to different operations: *Remove*, *Add*, *Replace*, *Modify*, *Rewrite*,
and *Others*. The annotators need to fill in the templates to generate the instructions.
6. **Correct summary**: Following the instruction
in 5., the annotator is required to **edit the initial
summary** to make it *factually consistent* with minimal, necessary modifications.

We use [XSum](https://github.com/EdinburghNLP/XSum) as the target dataset and [Pegasus](https://github.com/google-research/pegasus) as the pre-trained summarization model to generate the initial system outputs.

The dataset statistics are summarized below.

| | Train | Val | Test | All |
| --- | --- | --- | --- | --- |
| All |  1000 | 486 | 1075 | 2561 |
| w/ Errors | 701 | 341 | 779 | 1821 |

## Using DeFacto

We provide the data files in **`./data`** and a simple data loader **``data_loader.py``**.

Each line of the data files contain a data example stored in the Json format, with the following strucure:

```
 {
  "article": "input article",
  "abstract": "abstract/reference summary",
  "candidate": "candidate/initial system output",
  "doc_id": int,
  "has_error": true/false
  "intrinsic_error": true/false,
  "extrinsic_error": true/false,
  "feedback": {
    "summary": "human-corrected summary",
    "evidence": "selected sentence from the input article",
    "explanation": "natural language explanation",
    "instruction": "concatenated instructions",
    "instruction_list": ["list of instructions", ],
  },
}
```


## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
