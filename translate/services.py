from google.cloud import translate_v2 as translate


class GoogleTranslateService():

    translate_client = translate.Client()
    supported_languages = [lang["language"] for lang in translate_client.get_languages()]

    def translate(self, source_text: str, target_language: str, source_language=None) -> [str, str]:
        if target_language not in self.supported_languages:
            raise ValueError("Target language not supported")
        elif source_language and source_language not in self.supported_languages:
            raise ValueError("Source language not supported")
        result = self.translate_client.translate(source_text,
                                                 target_language=target_language,
                                                 source_language=source_language)
        target_text = result["translatedText"]
        if "detectedSourceLanguage" in result:
            source_language = result["detectedSourceLanguage"]
        return target_text, source_language
