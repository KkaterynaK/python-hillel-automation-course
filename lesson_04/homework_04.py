adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# task 01
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03
words = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = " ".join(words)

# task 04
h_count = adwentures_of_tom_sawer.count("h")
print(f"Літера 'h' зустрічається {h_count} разів.")

# task 05
words_list = adwentures_of_tom_sawer.split()
title_words_count = 0

for word in words_list:
    if word.istitle():
        title_words_count += 1

print(f"Кількість слів з великої літери: {title_words_count}")

# task 06
first_tom = adwentures_of_tom_sawer.find("Tom")
second_tom = adwentures_of_tom_sawer.find("Tom", first_tom + 1)

print(f"Позиція другого слова Tom: {second_tom}")

# task 07
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")

# task 08

fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
print(f"Четверте речення: {fourth_sentence}")

# task 09
starts_with_by_the_time = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        starts_with_by_the_time = True
        break

print(f"Чи починається якесь речення з 'By the time': {starts_with_by_the_time}")

# task 10
last_sentence = adwentures_of_tom_sawer_sentences[-1]
last_sentence_words_count = len(last_sentence.split())

print(f"Кількість слів в останньому реченні: {last_sentence_words_count}")
