
# The Change of Chinese Female Image in about the Past 20 Years -- Summarized by study 742 Women Magazine Covers
This repository was created in the Semester B of 2020-2021. It stores the group project of the course AIDM 7410 Computational Journalism @ Hong Kong Baptist University. This group project was created by LIN Meishan, FU Yu, HU Xinyu and ZHANG Chengxin.
# Data
We collected a total of 802 magazines, including 197 copies of For Him Magazine, 369 copies of COSMO, and 236 copies of WOMEN OF CHINA. We only selected the magazines with women on the cover, and after screening 802 magazines, 742 were left. Among them, the time span of FHM and COSMO is from 2004 to the present, and the WOMEN OF CHINA is from 2001 to the present. The pictures are all from public websites, but a few are missing. We use a combination of computer and human methods for data processing, computer methods for color analysis and text recognition on pictures, and human coding for the extraction of female character features. 

# Coding
Specific coding categories: name, year of birth, occupation, whether she is a star, skin color, region, scene, clothing, hairstyle, posture, whether to look at the camera, whether single. A total of three coders were cross validated. All the computer codes and man-made coding tables used can be found in the supporting files.

# Statistical analysis
Statistically analyze and visualize the encoded information.

# Text extraction
We used Baidu AI to identify the cover and extract the text from the cover. And use code to analyze and visualize the text.

# Color extraction
We extracted the 5 colors with the highest proportion in each cover and set the width according to the color ratio. The length of each color is 224 pixels. Then we sort the color maps according to their RGB mean value (color depth), one row spans one year, arranged from top to bottom, and synthesizes the color maps of the three magazines above. The missing parts of the magazine material are filled with white pictures.
# Report
The rendered report can be viewed here . [report](https://chenxinzhang.github.io/AIDM7410/)
