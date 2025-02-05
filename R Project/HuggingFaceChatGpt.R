# Install and load the httr package
install.packages("httr")
library(httr)

# Define your Hugging Face API key
hugging_face_api_key <- "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"

# Make a POST request to the Hugging Face Inference API using GPT-Neo
response <- POST(
  url = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B",  # Using GPT-Neo model
  add_headers(Authorization = paste("Bearer", hugging_face_api_key)),
  encode = "json",
  body = list(inputs = "where is India ?")
)

# Print the response
content(response, "text")
