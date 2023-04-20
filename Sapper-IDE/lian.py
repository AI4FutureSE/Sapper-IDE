import openai
openai.api_key = "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"

# response = openai.Completion.create(
# 	engine="text-davinci-003",
# 	prompt= "print(\"Hello world\")",
# 	temperature= 0.7,
# 	max_tokens=225,
# 	top_p=1,
# 	frequency_penalty=0,
# 	presence_penalty=0,
# 	stop=""
# )
ready_prompt = 'A lonely fisherman afloat,Is fishing snow in lonely boat.'
response1 = openai.Image.create(
	prompt=ready_prompt,
	n=1,
	size="512x512",
)
image_url = response1['data'][0]['url']

print(image_url)
