from TikTokApi import TikTokApi

api = TikTokApi.get_instance()

results = 50

trending = api.trending(count=results, custom_verifyFp="verify_kia5etc8_VyWC7Puw_Hp4K_4TXx_B74x_XKQnsdTV48lR")


for tiktok in trending:
    print(tiktok['user_name'])

print(len(trending))