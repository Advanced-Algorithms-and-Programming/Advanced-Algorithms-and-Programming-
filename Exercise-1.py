def analyze_message(message):
    uppercase_count = 0
    alpha_count = 0
    punctuation_count = 0
    repeat_count = 1
    has_spam_repeat = False

    for i in range(len(message)):
        ch = message[i]

   
        if ch.isalpha():
            alpha_count += 1
            if ch.isupper():
                uppercase_count += 1

   
        if ch == '!' or ch == '?':
            punctuation_count += 1

    
        if i > 0 and message[i] == message[i - 1]:
            repeat_count += 1
            if repeat_count > 3:
                has_spam_repeat = True
        else:
            repeat_count = 1

   
    if alpha_count > 0:
        caps_ratio = uppercase_count / alpha_count
    else:
        caps_ratio = 0

    if caps_ratio >= 0.6 or punctuation_count >= 5:
        category = "AGGRESSIVE"
    elif caps_ratio >= 0.3 or punctuation_count >= 3:
        category = "URGENT"
    else:
        category = "CALM"

    return uppercase_count, punctuation_count, caps_ratio, category, has_spam_repeat


if __name__ == "__main__":
    msg = input("Enter message: ")
    result = analyze_message(msg)

    print("Uppercase letters:", result[0])
    print("Punctuation count:", result[1])
    print("Caps ratio:", round(result[2], 2))
    print("Category:", result[3])
    print("Spam repeated characters:", result[4])