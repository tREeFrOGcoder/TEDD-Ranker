# Take the Essence and Discard the Dross: A Rethinking on Data Selection for Fine-Tuning Large Language Models

## ✨ Latest News
- [02/23/2025]: 🔨 Latest website and ranking algorithms addressed some minor errors in the **feasibility ranking plot** (Figure 5) and **feasibility rank table** (Appendix Table 5). Check out the updated Arxiv version [here](https://arxiv.org/pdf/2406.14115).
- [02/08/2025]: 🎉🎉🎉 Our paper has been accepted at **NAACL 2025**! The full paper is available [here](https://arxiv.org/pdf/2406.14115).
- [01/26/2025]: 👋 Our **TEDD-Ranker** visualization is now available! Check it out at [TEDD-Ranker](https://zicheliu.com/TEDD-Ranker/) with your own data selection methods!


## ⚡ Introduction
> 𝑸𝒖𝒂𝒍𝒊𝒕𝒚 𝒎𝒂𝒕𝒕𝒆𝒓𝒔 𝒎𝒐𝒓𝒆 𝒕𝒉𝒂𝒏 𝒒𝒖𝒂𝒏𝒕𝒊𝒕𝒚! 

Data selection for fine-tuning large language models has been a hit topic with various methods proposed over the last few years. For anyone intersted in the field or wish to develop new methods, some natural questions would be: **What are the existing methods** and **How good are they**?

Our work takes a retrospective look at a dozen key data selection techniques for fine-tuning LLMs, and introduces the following:

- A novel **three-stage scheme**, comprising **feature extraction**, **criteria design**, and **selector evaluation**, which systematically categorizes and evaluates these methods.
![ThreeStageScheme](assets/20250205ThreeStageScheme.png)
- a **unified comparison approach** that incorporates ratio-based efficiency and ranking-based feasibility metrics to address inconsistencies across evaluation settings.
![ComparisonFlow](assets/20250207ComparisonMethod.png)


## 💭 Results and Discussions
**TL;DR**: 
> 𝑴𝒆𝒕𝒉𝒐𝒅𝒔 𝒆𝒎𝒑𝒉𝒂𝒔𝒊𝒛𝒊𝒏𝒈 𝒎𝒐𝒓𝒆 𝒕𝒂𝒓𝒈𝒆𝒕𝒆𝒅 𝒒𝒖𝒂𝒍𝒊𝒕𝒚 𝒎𝒆𝒂𝒔𝒖𝒓𝒆𝒎𝒆𝒏𝒕 𝒂𝒄𝒉𝒊𝒆𝒗𝒆 𝒉𝒊𝒈𝒉𝒆𝒓 𝒆𝒇𝒇𝒊𝒄𝒊𝒆𝒏𝒄𝒚 𝒃𝒖𝒕 𝒂𝒕 𝒕𝒉𝒆 𝒄𝒐𝒔𝒕 𝒐𝒇 𝒇𝒆𝒂𝒔𝒊𝒃𝒊𝒍𝒊𝒕𝒚.
> \-- 𝒕𝒉𝒆 𝒂𝒖𝒕𝒉𝒐𝒓𝒔

The frameworks introduced above allow us to obtain a quantitative **Efficiency Rank Plot**, and a qualitative **Feasibility Rank Plot**.
![TwoGraphs](assets/20250223combined.png)

Integrating the detailed method analysis and these ranking results, we discuss the main trends from the perspective of **Candidate Dataset**, **Quality Measurement** and **Selected Features**; as well as a look into the future challenges and directions.
![Trend](assets/20250208Trend_tall_new.png)


## 🔗 TEDD-Ranker: Code & Visualization
We provide an **interactive visualization** of how we compute and visualize the efficiency and feasibility of data selection methods for easy comparison.
our method rankings and selection efficiency comparisons at:
🔗 [TEDD-Ranker Visualization](https://zicheliu.com/TEDD-Ranker/)

- **Efficiency Rank**: Performance Improvement Ratio (PIR) vs. Selected Dataset Fraction (SDF).
- **Feasibility Rank**: Simplicity and flexibility of each method.

*Note: The feasibility ranking table and feasibility rank plot contained minor errors in the original version. These are now corrected in the latest ArXiv update and TEDD-Ranker website.*

## 📈 Key Results


<div align=center>
<img src="assets/efficiency_feasibility_ranking.png" width = "640" alt="Efficiency vs. Feasibility" align=center/>
</div>



## 🧐 Limitations

- **Error Corrections**: Our feasibility ranking plot (Appendix Figure 5) had **minor ranking errors** in early versions. The website and **latest ArXiv version** are now correct.
- **Ongoing Updates**: TEDD-Ranker is evolving. We welcome feedback and **will update rankings with new datasets/methods**.
- **Contact for Fixes**: If you spot any inconsistencies, **email archerliu@berkeley.edu or treefrogorigami@gmail.com**. Confirmed errors will be corrected and updated.

## 🤝 Acknowledgements
This research is supported by:
- The School of Data Science, **The Chinese University of Hong Kong, Shenzhen**.
- **Shenzhen Research Institute of Big Data**.

## 📜 Citation
```bibtex
@article{liu2024take,
  title={Take the essence and discard the dross: A Rethinking on Data Selection for Fine-Tuning Large Language Models},
  author={Liu, Ziche and Ke, Rui and Jiang, Feng and Li, Haizhou},
  journal={arXiv preprint arXiv:2406.14115},
  year={2024}
}
```
<!-- 
## ⭐ Star History
<a href="https://star-history.com/#tREeFrOGcoder/TEDD-Ranker&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=tREeFrOGcoder/TEDD-Ranker&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=tREeFrOGcoder/TEDD-Ranker&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=tREeFrOGcoder/TEDD-Ranker&type=Date" />
  </picture>
</a> -->

