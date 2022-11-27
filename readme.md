# **Customer Clustering**

### This project is purpose to accomplish Machine Learning Course in Diponegoro University

## **Group Members**

| NIM            | Name                      |
| -------------- | ------------------------- |
| 24060120130044 | Alvin Triseptia Mairis    |
| 24060120130059 | Liem, Roy Marcelino       |
| 24060120140134 | Yusuf Qisthi Abdul Jabbar |
| 24060120       | Fariz                     |
| 24060120       | Daniel                    |

## **Introduction**

Customer Clustering is a process of grouping customers based on the characteristics they have. Thus, customers can be grouped into several groups that have the same characteristics.

## **Dataset**

The dataset is taken from [Kaggle](https://www.kaggle.com/datasets/dev0914sharma/customer-clustering)

The dataset contains 8 columns and 2000 rows. The columns are contains

- ID : id Pelanggan
- Sex : Jenis kelamin (0 = Laki-laki, 1 = Perempuan)
- Marital Status : Status perkawinan (0 = Single, 1 = Non-Single(Divorced / Separated / Married / Widowed)
- Age : Umur
- Education : Pendidikan (0 = Unknown / Other, 1 = High School, 2 = University, 3 = Graduate School)
- Income : Pendapatan
- Occupation : Pekerjaan (0 = Unemployed / Unskilled, 1 = Official Employee, 2 = Self-Employee)
- Settlement Size : Daerah Pemukiman (0 = Small City, 1 = Mid-sized City, 2 = Big City)

## **Clustering**

The model used in this project is K-Means Clustering. To know how we found the best model, go to our [Google Colab](https://colab.research.google.com/drive/1-_DDKFvqFVz6FHV-eHy59Cj-06iWkt28?usp=sharing#scrollTo=Qt3gbMz5O-qk)

## **Deployement**

For demo, go to our [Website Customer Clustering](https://customer-clustering.onrender.com/)

## **How to Contribute**

1. Fork this repository
2. Clone your forked repository
3. Create a new branch

```
    git checkout -b <branch-name>
```

4. Make changes and commit

```
    git add .
    git commit -m "<commit-message>"
```

5. Push changes to GitHub

```
    git push origin <branch-name>
```

6. Create a pull request

## **How to Run**

1. After cloning the repository, install the requirements

```
    pip install -r requirements.txt
```

2. Run the app

```
    flask run
```

## **Tech**

1. [Flask](https://flask.palletsprojects.com/en/2.0.x/)
2. [Tailwind CSS](https://tailwindcss.com/)
3. [Google Colab](https://colab.research.google.com/)
4. [Render](https://render.com/)
