# Item-Based Movie Recommendation System

This repository contains the implementation of an item-based collaborative filtering recommendation system for movies. The system is built to predict movies that a user might like based on the ratings they have given to other movies.

**Key Features:**

* **Item-Based Collaborative Filtering:** Implements the logic to find similar movies based on user ratings and generate recommendations.
* **Evaluation Metrics:** Includes functions to evaluate the performance of the recommender using:
    * **Precision@k:** Measures the relevance of the top k recommendations.
    * **Recall@k:** Measures the proportion of relevant movies found in the top k recommendations.
    * **F1-score@k:** Provides a balanced measure of precision and recall.
* **Parameter Tuning:** Allows for experimentation with key parameters such as:
    * **k:** The number of top recommendations to consider during evaluation.
    * **num_similar_items:** The number of most similar items to consider when generating recommendations.
* **Performance Analysis:** Contains scripts and potentially notebooks to run evaluations for different parameter combinations and visualize the results.
* **Visualizations:** Includes heatmaps illustrating the variation of Precision@k, Recall@k, and F1-score@k as `k` and `num_similar_items` are varied.

**Potential Use Cases:**

This repository can be useful for:

* Individuals learning about recommendation systems and collaborative filtering techniques.
* Data science enthusiasts looking for a practical implementation of an item-based recommender.
* Anyone interested in understanding the impact of different parameters on the performance of a recommendation system.

**Further Exploration (Optional):**

Future work could include:

* Trying different item similarity metrics.
* Implementing user-based collaborative filtering for comparison.
* Exploring techniques to address data sparsity or the cold-start problem.
* Evaluating with other recommendation metrics like Average Precision or NDCG.

**Visualizations:**

Heatmaps visualizing the performance metrics across different parameter settings can be found in the repository (e.g., `image_be2d22.png`, `image_bdd6cb.png`, `image_bdd6a8.png`).
