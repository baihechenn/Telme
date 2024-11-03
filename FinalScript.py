import pickle
import numpy as np

# Load all necessary models and encoders
with open('kmeans_model.pkl', 'rb') as f:
    kmeans_model = pickle.load(f)

with open('logistic_model.pkl', 'rb') as f:
    logistic_model = pickle.load(f)

with open('city_encoder.pkl', 'rb') as f:
    city_encoder = pickle.load(f)

with open('plan_encoder.pkl', 'rb') as f:
    plan_encoder = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Updated function to assign cluster with the correct number of features
def assign_cluster(days_since_joining, total_plan_changes, city):
    # Encode the city
    city_encoded = city_encoder.transform([city])[0]

    # Placeholder encoded values for the missing plan features (e.g., 0 = Basic plan)
    encoded_phone_plan = 0  # Assume basic phone plan for new users
    encoded_internet_plan = 0  # Assume basic internet plan for new users
    encoded_cable_plan = 0  # Assume basic cable plan for new users

    # Prepare the user input with the correct number of features (5 features)
    user_features = np.array([[days_since_joining, total_plan_changes, 
                               encoded_phone_plan, encoded_internet_plan, 
                               encoded_cable_plan]])

    # Scale the input features
    user_features_scaled = scaler.transform(user_features)

    # Predict the cluster using the K-means model
    predicted_cluster = kmeans_model.predict(user_features_scaled)[0]
    print(f"User assigned to Cluster: {predicted_cluster}")

    return predicted_cluster

# Function to recommend a plan based on the cluster and city
def recommend_plan(cluster, city):
    # Encode the city
    city_encoded = city_encoder.transform([city])[0]

    # Prepare input features for the Logistic Regression model
    plan_features = np.array([[cluster, city_encoded]])

    # Predict the plan using the logistic regression model
    predicted_plan = logistic_model.predict(plan_features)[0]

    # Decode the predicted plan
    recommended_plan = plan_encoder.inverse_transform([predicted_plan])[0]

    print(f"Recommended Plan: {recommended_plan}")
    return recommended_plan

# Main function to interact with the user
def main():
    print("Welcome to the Plan Recommendation System!")
    
    # Collect user input
    city = input("Enter your city: ").strip()
    days_since_joining = int(input("Enter the number of days since joining (0 for new user): "))
    total_plan_changes = int(input("Enter the number of plan changes (0 for new user): "))

    # Assign the user to a cluster with the correct feature inputs
    user_cluster = assign_cluster(days_since_joining, total_plan_changes, city)

    # Recommend a plan based on the user's cluster and city
    recommended_plan = recommend_plan(user_cluster, city)

    print(f"Based on your input, we recommend the following plan: {recommended_plan}")

# Run the main function
if __name__ == '__main__':
    main()
