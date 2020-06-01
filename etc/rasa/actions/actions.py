from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from actions.setup_qa import (
    #question_answering_pipeline,
    search_article,
    extract_text,
    final_text,
)



class ActionGetUserAge(Action):

    def name(self) -> Text:
        return "action_userage"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        age=tracker.get_slot("userage")
        
        if int(age)<30:
            dispatcher.utter_message("Вы так молоды!")
        elif int(age)>=30:  
            dispatcher.utter_message("Очень хороший возраст!")

           
        
class ActionGetUserBirthPlace(Action):

    def name(self) -> Text:
            return "action_birthplace"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        birthplace=tracker.get_slot("birthplace")
        west_kz=["Атырау","Актау","Актобе","Жанаозен","Уральск"]
        east_kz=["Усть-Каменогорск","Семей","Зайсан","Урджар"]
        north_kz=["Астана","Нур-Султан","Петропавл","Павлодар","Кокшетау"]
        south_kz=['Алматы','Кызылорда','Шымкент','Тараз']
        central_kz=["Караганда"]
        
        if birthplace in west_kz:
            dispatcher.utter_message("ОО вы из нефтяного края")
        elif birthplace in east_kz:
            dispatcher.utter_message("Мне очень нравиться Алакол!")
        elif birthplace in north_kz:
            dispatcher.utter_message("Красота Бурабая это нечто!")
        elif birthplace in south_kz:
            dispatcher.utter_message("Очень люблю южные города Казахстана!")
        elif birthplace in central_kz:
            dispatcher.utter_message("Наслышан о степях центрального Казахстане!")
        else:
            dispatcher.utter_message("К сожалению не знаю такой город.Расскажите о вашем городе?")

class ActionTellTale(Action):

    def name(self) -> Text:
        return "action_tale"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        query = "Русские сказки"
        dispatcher.utter_message(final_text(query))
     
        
        
    
class ActionFilmRecommendation(Action):

    def name(self) -> Text:
        return "action_film"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        filmgenre=tracker.get_slot("filmgenre")
        query="Фильмы жанра "+filmgenre
        dispatcher.utter_message(final_text(query))
        
        
class ActionBookRecommendation(Action):

    def name(self) -> Text:
        return "action_book"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        bookgenre=tracker.get_slot("bookgenre")
        query="Книги про "+bookgenre
        dispatcher.utter_message(final_text(query))
        
        
        
class ActionTranslate(Action):

    def name(self) -> Text:
        return "action_translate"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("translate.google.com")
        
class ActionFoodRecommandation(Action):

    def name(self) -> Text:
        return "action_cooking"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        query=tracker.get_slot("cooking")
        dispatcher.utter_message(final_text(query))
     
        
class ActionNotFound(Action):

    def name(self) -> Text:
        return "action_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        query=tracker.latest_message.get('text')
        dispatcher.utter_message(final_text(query))
        
        
        
                
class ActionUserLovelyFood(Action):

    def name(self) -> Text:
        return "action_userlovelyfood"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text=tracker.get_slot("user_lovely_food")
        query="Интересные факты про "+text
        dispatcher.utter_message(final_text(query))
        
        
        
class ActionUserLovelyFood(Action):

    def name(self) -> Text:
        return "action_userlovelysport"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text=tracker.get_slot("user_lovely_food")
        query="Интересные факты про "+text
        dispatcher.utter_message(final_text(query))
        
        
   
                
class ActionUserBirthDate(Action):

    def name(self) -> Text:
        return "action_userbirthdate"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        bd=tracker.get_slot("user_birthdate")
        month=bd.split('.')[1]
        if month=='01':
            dispatcher.utter_message("Люди, рожденные в первый месяц года, наделены твердым характером и непробиваемой силой воли. Даже если это самая легкая и воздушная девушка, не обольщайтесь — ее характер не сломят никакие препятствия. Самые невероятные трудности жизни январские именинники переносят достойно, с гордо поднятой головой. По натуре они лидеры и неосознанно ищут рядом с собой человека, который бы смог соперничать с ними. Решительные, уверенные в себе и отзывчивые, рожденные в январе люди больше всего, как ни странно, страдают от своей силы — им порой бывает сложно найти людей, которые бы соответствовали им по масштабу и которые могли бы так же четко следовать своим принципам.")
        elif month=="02":
            dispatcher.utter_message("Февральские именинники кажутся невероятно обаятельными романтиками, но за этой маской скрываются немного эгоистичные люди, у которых много идей и очень мало выполненных дел. Рожденные в феврале могут быть как элегатными снобами, так и интеллигентнейшими людьми, которые готовы дарить миру добро и радость. Впрочем, и те, и другие страдают от переменчивости настроения и являются непредсказуемыми людьми, что сильно мешает им в карьере и в личной жизни.")
        elif month=="03":
            dispatcher.utter_message("Добрые, порядочные, ранимые, восприимчивые, рожденные в марте люди с трудом переносят критику и могут прорыдать всю ночь, если их обидят. Это мнительные, чувствительные и порой нерешительные люди, которые могут быть вполне успешны, если совладают со своими нервами. В случае же, если они идут на поводу у эмоций, то в их жизни может случиться затяжная депрессия. Впрочем, в самых принципиальных вопросах эти люди бывают порой даже более бескопромиссными, чем рожденные в январе и апреле.")
        elif month=="04":
            dispatcher.utter_message("Апрельские люди — это невероятные материалисты и удивительные храбрецы. Кажется, они не боятся ничего! Апрельские именинники решительны, уверены в себе, они прирожденные лидеры, и порой в припадке своих бесконечных идей и планов могут забыть о тактичности и деликатности. Про женщин, рожденных в апреле, можно сказать, что «она коня на скаку остановит». Мужчины и вовсе могут добиться самых небывалых карьерных высот, сметая все на своем в пути. При этом в любви они очень страстные и нежные, поскольку так или иначе стремятся к душевному равновесию.")
        elif month=="05":
            dispatcher.utter_message("Упертые, бескомпромиссные, родившиеся в мае с трудом идут на уступки, любят власть и контроль. При этом с ними можно договориться, используя логику и железные аргументы. Настроение майских именинников переменчиво, но в общем и целом они стабильны — верные, надежные и принципиальные люди. В любви они, как правило, очень страстные, а в карьере достигают невероятных высот. Угнаться за майскими людьми практически невозможно.")
        elif month=="06":
            dispatcher.utter_message("Июньские именинники очень ранимые, но скрывают это за броней комплексов.Это люди информации, идей, сплетен, капризов и перемены настроений.  Это яркие и талантливые люди, прекрасные ораторы и харизматичные лидеры, которые, впрочем, подвержены множеству пороков. Если июньские именинники смогут победить свои слабости с помощью силы воли, то их ждет самое блестящее будущее.")
        elif month=="07":
            dispatcher.utter_message("Сложные, противоречивые, многогранные, таинственные, июльские именинники больше любых других стремятся к независимости и свободе, но, получив ее, не всегда знают, что с ней делать. Парадокс в том, что, будучи свободолюбивыми людьми, сами они очень любят устанавливать контроль и свои правила. Прийти со своим уставом в чужой монастырь — это про них. Рожденные в июле — невероятные эгоисты, но настолько обаятельные, что часто им это сходит с рук. Эти люди умеют любить и дружить, однако в глубине души смотрят на всех свысока.")
        elif month=="08":
            dispatcher.utter_message("Рожденные в августе — страстные и эмоциональные натуры, знающие толк в чувственных удовольствиях и умеющие жить ярко, на широкую ногу. Их отличает эмоциональность и энергичность, к ним тянутся люди, вокруг них всегда происходят самые интересные события, но зачастую, будучи лидерами по натуре и душой компании, эти люди становятся жертвами интриг из-за своей доверчивости. Впрочем, природное обаяние помогает им выходить из любой ситуации с высоко поднятой головой.")
        elif month=="09":
            dispatcher.utter_message("Люди, рожденные в сентябре, добиваются огромных успехов в бизнесе и больше остальных имеют шансы заработать действительно огромные деньги. В их голове настоящий калькулятор, который отвечает за расчетливость и практичность. При этом сентябрьские натуры умеют получать удовольствие от жизни и точно знают, ради чего все эти усилия — их любовь к достатку и комфорту идет от большой любви к себе.")
        elif month=="10":
            dispatcher.utter_message("Сложные, переменчивые, внешне эти люди кажутся простейшими добряками, но едва вы копнете глубже — увидите противоречивую смесь самого разного рода эмоций, свойственную творческим натурам. Они во всем сомневаются, при этом без постоянной эмоциональной подпитки чахнут, поэтому спокойной жизни рядом с рожденными в октябре ждать не приходится. Бонусом общения с ними является попадание в водоворот интересных жизненных ситуаций — приключений с ними не избежать.")
        elif month=="11":
            dispatcher.utter_message("Настоящий ящик Пандоры, люди ноября — самые загадочные личности из всех 12 типов. Сила воли, харизма и интеллект — вот три кита, на которых базируется характеристика этих многогранных людей. Среди рожденных в ноябре — огромное количество роковых женщин и опасных мужчин, обаятельных манипуляторов, которые действуют на окружающих как магнит. Если бы не внутренние страхи и чрезмерные амбиции, они могли бы покорить мир. Не всем удается выпутаться из отношений с таким человеком без потерь — тихой гавани с ноябрьским именинником не ждите.")
        else:
             dispatcher.utter_message("Мудрые, сильные и практичные, рожденные в декабре люди кажутся оплотом рассудительности и здравого смысла. Но не все так просто в этой жизни. Декабрьские именинники — страшные идеалисты, которые во имя благих целей могут сметать все на своем пути. Сломить их нелегко, но сами они, попадая в вихрь страстей и собственных непростых представлений о жизни, любви и добре и зле, часто получают неприятные жизненные уроки. Среди рожденных в декабре очень много авторитетных людей, чьему мнению доверяет большинство. Сами они склонны менять свои убеждения с возрастом.")
            
class ActionMusicRecommendation(Action):

    def name(self) -> Text:
        return "action_music"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text=tracker.get_slot("musicgenre")
        query="Музыка "+text
        dispatcher.utter_message(final_text(query))
        

                
class ActionGetUserName(Action):

    def name(self) -> Text:
        return "action_username"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name=tracker.latest_message.get('text')
        dispatcher.utter_message("Как ваши дела "+name+" ?")
        return [SlotSet("username", name)]
        
       