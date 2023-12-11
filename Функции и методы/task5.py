def get_sentences_list(text):
    sentences_list = []
    for sentences in text.split("."):
        if sentences:
            sentences_list.append(sentences.strip())
    return sentences_list



print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
