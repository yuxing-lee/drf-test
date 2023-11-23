from google.cloud import translate_v2 as translate

translate_client = translate.Client()


def translate_text(text, target="zh-TW"):
    result = translate_client.translate(text, target_language=target)
    return {
        "source_text": text,
        "target_text": result["translatedText"],
        "source_language": result["detectedSourceLanguage"],
        "target_language": target
    }
