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
ready_prompt = '一个程序员坐在电脑前，一个客户站在程序员身旁，他们两个正在讨论程序开发的需求，程序员的电脑前面是一个绚丽的颜色，让他们的故事充满了活力，动画风格，把他们的故事生动地展现出来'
response1 = openai.Image.create(
	prompt=ready_prompt,
	n=1,
	size="512x512",
)
image_url = response1['data'][0]['url']

print(image_url)
