import urllib.request, json, datetime

print("Proper pack EV (Estimated Value) after sellling rares, uncommons and converting all cheap cards to tickets. Press Enter to repeat search")

CARD_LOWEST_PRICE = 0.04
CARD_LOWEST_PRICE_RU = 0.02

while True:
  price = {}

  avg_common_price = 0
  avg_uncommon_price = 0
  avg_rare_price = 0

  avg_rare_hero = 0
  with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?q=&category_583950_Card_Type%5B%5D=tag_Hero&category_583950_Rarity%5B%5D=tag_Rarity_Rare&appid=583950&norender=1&count=1000") as url:
    data = json.loads(url.read().decode())
  i = 0
  for entry in data['results']:
    i += 1
    price[entry['name']] = entry['sell_price']/100
    avg_rare_hero += price[entry['name']]
  avg_rare_hero = avg_rare_hero / i

  avg_rare_spell = 0
  with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?q=&category_583950_Card_Type%5B%5D=tag_Spell&category_583950_Rarity%5B%5D=tag_Rarity_Rare&appid=583950&norender=1&count=1000") as url:
    data = json.loads(url.read().decode())
  i = 0
  for entry in data['results']:
    i += 1
    price[entry['name']] = entry['sell_price']/100
    avg_rare_spell += price[entry['name']]
  avg_rare_spell = avg_rare_spell / i

  avg_rare_item = 0
  with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?q=&category_583950_Card_Type%5B%5D=tag_Item&category_583950_Rarity%5B%5D=tag_Rarity_Rare&appid=583950&norender=1&count=1000") as url:
    data = json.loads(url.read().decode())
  i = 0
  for entry in data['results']:
    i += 1
    price[entry['name']] = entry['sell_price']/100
    avg_rare_item += price[entry['name']]
  avg_rare_item = avg_rare_item / i

  avg_rare_creep = 0
  with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?q=&category_583950_Card_Type%5B%5D=tag_Creep&category_583950_Rarity%5B%5D=tag_Rarity_Rare&appid=583950&norender=1&count=1000") as url:
    data = json.loads(url.read().decode())
  i = 0
  for entry in data['results']:
    i += 1
    price[entry['name']] = entry['sell_price']/100
    avg_rare_creep += price[entry['name']]
  avg_rare_creep = avg_rare_creep / i

  avg_rare_improvement = 0
  with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?q=&category_583950_Card_Type%5B%5D=tag_Improvement&category_583950_Rarity%5B%5D=tag_Rarity_Rare&appid=583950&norender=1&count=1000") as url:
    data = json.loads(url.read().decode())
  i = 0
  for entry in data['results']:
    i += 1
    price[entry['name']] = entry['sell_price']/100
    avg_rare_improvement += price[entry['name']]
  avg_rare_improvement = avg_rare_improvement / i

  # https://www.reddit.com/r/Artifact/comments/9zld8l/more_pack_stats_plus_market_predictions/
  # 0.0833 rare heroes
  # 0.1666 rare items
  # 0.2019 rare creeps
  # 0.2452 rare improvements
  # 0.3029 rare spells
  rare_EV = 0.0833 * avg_rare_hero + 0.1666 * avg_rare_item + 0.2019 * avg_rare_creep + 0.2452 * avg_rare_improvement + 0.3029 * avg_rare_spell

  avg_uncommon_price = 0
  avg_uncommon_price_ru = 0
  with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?search_descriptions=0&category_583950_Rarity%5B%5D=tag_Rarity_Uncommon&sort_dir=desc&appid=583950&norender=1&count=1000") as url:
    data = json.loads(url.read().decode())
  i = 0
  for entry in data['results']:
    i += 1
    raw_price = entry['sell_price']/100
    after_sale = raw_price
    #tax1
    if (0.10 * raw_price > 0.01):
      after_sale -= 0.10 * raw_price
    else:
      after_sale -= 0.01
    #tax2
    if (0.05 * raw_price > 0.01):
      after_sale -= 0.05 * raw_price
    else:
      after_sale -= 0.01
    #lowest floor
    if after_sale < CARD_LOWEST_PRICE:
      after_sale = CARD_LOWEST_PRICE
    avg_uncommon_price += after_sale
    avg_uncommon_price_ru += raw_price
  avg_uncommon_price = avg_uncommon_price / i
  avg_uncommon_price_ru = avg_uncommon_price_ru / i

  # 7.6 commons per pack, 3.23 uncommons and 1.176 rares per pack
  # pack_EV == converting all commons to tickets, selling uncommons, KEEPING rares
  pack_EV = 7.6 * CARD_LOWEST_PRICE + 3.23 * avg_uncommon_price + 1.176 * rare_EV
  # pack_EV_mod == converting all commons to tickets, selling uncommons and rares
  pack_EV_mod = 7.6 * CARD_LOWEST_PRICE + 3.23 * avg_uncommon_price + 1.176 * rare_EV * 0.85
  # pack_EV_mod_ru == converting all commons to tickets, selling uncommons and rares @ ru market (no bullshit with 0.01 tax conversion)
  pack_EV_mod_ru = 7.6 * CARD_LOWEST_PRICE_RU + 3.23 * avg_uncommon_price_ru * 0.85 + 1.176 * rare_EV * 0.85

  print(f"[ {datetime.datetime.now().strftime('%m-%d %H:%M ')}] - fill collection pack EV - {pack_EV:.2f} $ - sell rares pack EV - {pack_EV_mod:.2f} $ - sell rares pack EV (non US market) - {pack_EV_mod_ru:.2f} $")
  input()
