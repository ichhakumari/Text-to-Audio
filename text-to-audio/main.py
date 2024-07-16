from text_to_speech import save

text = "Hello, Ichha! Nice to meet you , you are sooo beautiful! , lets catchup soon"
language = "en"  # Specify the language (IETF language tag)
output_file = "hello_ichha2.mp3"  # Specify the output file (only accepts .mp3)

save(text, language, file=output_file)
