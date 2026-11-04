# Datasets

Pick one of the eight datasets below at kickoff and keep it for all four tasks. All of them fit a laptop CPU; the level column is a rough guide to how much extra work the data type needs.

| Type | Dataset | Size | Task | License |
| ---- | ------- | ---- | ---- | ------- |
| Tabular | Adult Census Income | ~48k rows, 14 features | Classification | CC BY 4.0 |
| Tabular | Bank Marketing | ~45k rows, 16 features | Classification | CC BY 4.0 |
| Tabular | Bike Sharing | ~17k rows, 13 features | Regression | CC BY 4.0 |
| Time series | Engine degradation | ~130k cycle rows, 218 engines | Remaining useful life | US Government Works |
| Time series | Jena Climate 2009–2016 | ~420k rows, 14 features | Forecasting | See source |
| Graph | Arxiv | ~169k nodes, ~1.2M edges | Node classification | ODC-BY |
| Graph | Drug-drug interaction (ddi) | ~4.3k nodes, ~1.3M edges | Link prediction | CC0 |

## Dataset description

**Adult Census Income** — Records from the 1994 US Census. Predict whether a person earns more than 50K a year.

**Bank Marketing** — Phone marketing campaigns of a Portuguese bank. Predict whether a client subscribes to a term deposit.

**Bike Sharing** — Hourly and daily bike rental counts with weather and calendar information. Predict rental demand.

**Engine degradation** — Simulated multivariate sensor series from a fleet of aircraft engines. Predict how many operating cycles an engine has left.

**Jena Climate** — Weather measurements recorded every 10 minutes at a station in Jena, Germany. Forecast weather conditions.

**Arxiv** — Citation network of computer science papers on arXiv. Predict each paper's subject area.

**Drug-drug interaction** — Network of known drug-drug interactions. Predict which drug pairs interact.

All datasets fit on a laptop CPU. Each keeps its original license: cite the source in your reports.

## Data licenses

The datasets are **not** covered by this repository's own license. Each one is redistributed under the terms set by its owner; if you use or share it, follow those terms and cite the source as shown below.

**Changes to the original data:** datasets for this hands-on have been modified for the purpose of the exercise.

- **Adult Census Income** — [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
  Becker, B. & Kohavi, R. (1996). *Adult* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5XW20

- **Bank Marketing** — [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
  Moro, S., Rita, P. & Cortez, P. (2014). *Bank Marketing* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5K306

- **Bike Sharing** — [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
  Fanaee-T, H. (2013). *Bike Sharing* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894
  The dataset authors also ask publications to cite: Fanaee-T, H. & Gama, J. (2013). Event labeling combining ensemble detectors and background knowledge. *Progress in Artificial Intelligence*, 1–15. https://doi.org/10.1007/s13748-013-0040-3

- **Engine degradation** — U.S. Government Work, public domain in the United States ([details](https://www.usa.gov/government-copyright)).
  Saxena, A. & Goebel, K. (2008). *PHM08 Challenge Data Set*. NASA Prognostics Data Repository, NASA Ames Research Center, Moffett Field, CA. https://data.nasa.gov/dataset/phm-2008-challenge

- **Jena Climate 2009–2016** — No license stated by the data owner, so this dataset is **not included** in the repository. Download it from [Kaggle](https://www.kaggle.com/datasets/mnassrib/jena-climate) or from the [weather station of the Max Planck Institute for Biogeochemistry](https://www.bgc-jena.mpg.de/wetter/).
  Source: Max Planck Institute for Biogeochemistry, Jena, Germany.

- **Arxiv** — [ODC-BY 1.0](https://opendatacommons.org/licenses/by/1-0/).
  Hu, W., Fey, M., Zitnik, M., Dong, Y., Ren, H., Liu, B., Catasta, M. & Leskovec, J. (2020). Open Graph Benchmark: Datasets for Machine Learning on Graphs. *NeurIPS 2020*. https://arxiv.org/abs/2005.00687
  Wang, K., Shen, Z., Huang, C., Wu, C.-H., Dong, Y. & Kanakia, A. (2020). Microsoft Academic Graph: When experts are not enough. *Quantitative Science Studies*, 1(1), 396–413.

- **Drug-drug interaction** — [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/); no attribution required, citation appreciated.
  Hu, W. et al. (2020). Open Graph Benchmark: Datasets for Machine Learning on Graphs. *NeurIPS 2020*. https://arxiv.org/abs/2005.00687
  Wishart, D. S. et al. (2018). DrugBank 5.0: a major update to the DrugBank database for 2018. *Nucleic Acids Research*, 46(D1), D1074–D1082.

