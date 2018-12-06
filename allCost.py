import urllib.request, json, datetime

url_prefix = "https://steamcommunity.com/market/search/render/?search_descriptions=0&category_583950_Rarity%5B%5D="
url_suffix = "&sort_dir=desc&appid=583950&norender=1&count=500"
url_common = "tag_Rarity_Common"
url_uncommon = "tag_Rarity_Uncommon"
url_rare = "tag_Rarity_Rare"

print("Total market price for commons, uncommons and rares. Press Enter to repeat search")

while True:
  price = {}
  avg_common_price = 0
  avg_uncommon_price = 0
  avg_rare_price = 0

  with urllib.request.urlopen(url_prefix + url_common + url_suffix) as url:
    data = json.loads(url.read().decode())
  i = 0
  for entry in data['results']:
    i += 1
    price[entry['name']] = entry['sell_price']/100
    avg_common_price += price[entry['name']]
  if i == 0:
    avg_common_price = 0.0
  else:
    avg_common_price = avg_common_price / i

  with urllib.request.urlopen(url_prefix + url_uncommon + url_suffix) as url:
    data = json.loads(url.read().decode())
  i = 0
  for entry in data['results']:
    i += 1
    price[entry['name']] = entry['sell_price']/100
    avg_uncommon_price += price[entry['name']]
  if i == 0:
    avg_uncommon_price = 0.0
  else:
    avg_uncommon_price = avg_uncommon_price / i

  with urllib.request.urlopen(url_prefix + url_rare + url_suffix) as url:
    data = json.loads(url.read().decode())
  i = 0
  for entry in data['results']:
    i += 1
    price[entry['name']] = entry['sell_price']/100
    avg_rare_price += price[entry['name']]
  if i == 0:
    avg_rare_price = 0.0
  else:
    avg_rare_price = avg_rare_price / i

  heroes = ["Axe", "Bristleback", "Drow Ranger", "Kanna", "Lich", "Tinker", "Legion Commander", "Lycan", "Phantom Assassin", "Omniknight", "Luna", "Bounty Hunter", "Ogre Magi", "Sniper", "Treant Protector", "Beastmaster", "Enchantress", "Sorla Khan", "Chen", "Zeus", "Ursa", "Skywrath Mage", "Winter Wyvern", "Venomancer", "Prellex", "Earthshaker", "Magnus", "Sven", "Dark Seer", "Debbi the Cunning", "Mazzie", "J'Muy the Wise", "Fahrvhan the Dreamer", "Necrophos", "Centaur Warrunner", "Abaddon", "Viper", "Timbersaw", "Keefe the Bold", "Tidehunter", "Crystal Maiden", "Bloodseeker", "Pugna", "Lion", "Storm Spirit", "Meepo", "Rix", "Outworld Devourer"]

  total = 0.0
  for cost in price:
      if cost in heroes:
          total += price[cost]
      else:
          total += 3 * price[cost]

  print(f"[ {datetime.datetime.now().strftime('%m-%d %H:%M ')}] - average common - {avg_common_price:{3}.{3}}, uncommon - {avg_uncommon_price:{3}.{3}}, rare - {avg_rare_price:{3}.{3}}, TOTAL - {total:.2f} $")
  input()
