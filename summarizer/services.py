import re
import nltk
import sklearn
import transformers
import youtube_transcript_api
from nltk.corpus import stopwords
from youtube_transcript_api import YouTubeTranscriptApi
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import BartTokenizer, BartForConditionalGeneration


class SummarizerService:
    @staticmethod
    def get_youtube_transcript(link: str) -> str:
        video_id = link.split("=")[-1]
        subtitle = YouTubeTranscriptApi.get_transcript(video_id=video_id)
        joined_subtitles = " ".join([sub["text"] for sub in subtitle])
        return joined_subtitles

    @staticmethod
    def bart_summarization(text: str, percent: int) -> str:
        tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
        model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

        total_length = len(text.split(" "))
        required_length = (total_length * percent) // 100

        input_tensor = tokenizer.encode(text, return_tensors="pt", truncation=True)
        outputs_tensor = model.generate(
            input_tensor,
            max_length=required_length + 60,
            min_length=required_length,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True,
        )

        result = tokenizer.decode(outputs_tensor[0])
        return result

    @staticmethod
    def tf_idf_summarization():
        pass

    @staticmethod
    def summarize_wikipedia_articles(query: str):
        pass

    @staticmethod
    def summarize_news_articles():
        pass


link = "https://www.youtube.com/watch?v=_GInHEGqbos"
# a = SummarizerService.get_youtube_transcript(link)
text = """Above Uzbekistan, a masked former member of the League of Shadows, Bane, leads an attack on a CIA plane to abduct Russian nuclear physicist, Dr. Leonid Pavel, while planting a corpse as the scientist's decoy before crashing the aircraft.

Meanwhile, it has been eight years after the death of District Attorney Harvey Dent,[N 1] and organized crime has been eradicated in Gotham City thanks to legislation giving expanded powers to the police. Police commissioner James Gordon has kept Dent's killing spree as "Two-Face" a secret and allowed the blame for his crimes to fall on Batman. Gordon has prepared a speech revealing the truth but hesitates to read it at a public celebration. Bruce Wayne, still mourning the death of Rachel Dawes, has become a recluse and Wayne Enterprises is behindhand. Bane enlists Bruce's corporate rival John Daggett to buy Bruce's fingerprints. Daggett hires cat burglar Selina Kyle to steal Bruce's prints from Wayne Manor, but she is double-crossed by him and alerts the police.

The police arrive and pursue Bane and Daggett's henchmen into the sewers while Kyle flees. The henchmen capture Gordon and take him to Bane, but he escapes and is found by officer John Blake. Blake, an orphan who has figured out Bruce's secret identity, persuades him to return as Batman. Bane attacks the Gotham Stock Exchange and uses Bruce's fingerprints in a series of fraudulent transactions that leaves Bruce bankrupt. Batman resurfaces while intercepting Bane and his subordinates. Bruce's butler, Alfred Pennyworth, fears that Bruce will get himself killed fighting Bane, and resigns in the hope of saving him, but only after admitting that he burned a letter that Rachel left for him saying she was going to marry Dent. Bane expands his operations and kills Daggett while Bruce and Wayne Enterprises' new CEO Miranda Tate become lovers.

Kyle agrees to take Batman to Bane, but instead leads him into Bane's trap. Bane gloats that he intends to fulfill Ra's al Ghul's mission to destroy Gotham City before defeating Batman, then breaks his back before taking him abroad to an underground prison where escape is virtually impossible. The inmates tell Bruce the story of Ra's al Ghul's child, who was born and raised in the prison before escaping — the only prisoner to have done so. Bane traps the police forces in the sewers and destroys all but one bridge surrounding the city. He kills Mayor Anthony Garcia and forces Pavel to convert a fusion reactor core into a decaying neutron bomb before killing him. Outside Blackgate Penitentiary, Bane reads Gordon's speech to a crowd, revealing the truth about Dent. He releases the prisoners of Blackgate, instates martial law in the city, and exiles and kills Gotham's elite in kangaroo courts presided over by Jonathan Crane.

Five months later, Bruce escapes (after two prisoners adjusted his herniated disc back into place) and returns to Gotham. As Batman, he frees the police and they clash with Bane's army in the streets; during the battle, Batman overpowers Bane. Tate intervenes and stabs Batman, revealing herself as Talia al Ghul, Ra's al Ghul's daughter. She attempts to activate the bomb's detonator, but the bomb fails to activate due to Gordon blocking the signal. Talia leaves to find the bomb while Bane prepares to kill Batman, but Kyle arrives and kills Bane. Batman and Kyle pursue Talia, hoping to bring the bomb back to the reactor chamber where it can be stabilized. Talia's truck crashes, but she remotely floods and destroys the reactor chamber before dying. With no way to stop the detonation, Batman uses his aerial craft, the Bat, to haul the bomb far over the bay, where it safely explodes. Before takeoff, Batman subtly reveals his identity to Gordon.

In the aftermath, Batman is presumed dead and honored as a hero. Wayne Manor becomes an orphanage and Bruce's estate is left to Alfred. Gordon finds the Bat Signal repaired, while Lucius Fox discovers that Bruce had fixed the malfunctioning auto-pilot on the Bat. While traveling abroad, Alfred glimpses Bruce alive and in a relationship with Selina Kyle - they quietly acknowledge one other but move on without speaking. Blake, whose legal first name is revealed as Robin, resigns from the GCPD and receives a parcel from Bruce leading him to the Batcave.

"""
print("============================================================================")
SummarizerService.bart_summarization(text, 20)
