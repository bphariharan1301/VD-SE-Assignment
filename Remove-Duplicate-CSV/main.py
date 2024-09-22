import pandas as pd
import re


def is_valid_email(email):
    # Regular expression for validating an Email
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email) is not None


input_file = "user_data.csv"
output_file = "cleaned_user_data.csv"
df = pd.read_csv(input_file)


df_cleaned = df.drop_duplicates(subset="user_id")

df_cleaned = df_cleaned[df_cleaned["email"].apply(is_valid_email)]


df_cleaned.to_csv(output_file, index=False)

print(f"Cleaned data has been written to {output_file}.")
