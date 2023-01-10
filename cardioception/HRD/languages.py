#-*- coding:utf-8 -*-

# Author: Nicolas Legrand <nicolas.legrand@cfin.au.dk>
# Korean version : June Kang <june.kang@empathy-research.org>

from typing import Collection, Dict


def english(device: str, setup: str, exteroception: bool) -> Dict[str, Collection[str]]:
    """Create the text dictionary with instruction in Danish

    Parameters
    ----------
    device : str
        Can be `"keyboard"` or `"mouse"`.
    setup : str
        The experimental setup. Can be `"behavioral"` or `"test"`.
    exteroception : bool
        If `True`, the task includes and exteroceptive control condition.

    Returns
    -------
    texts : dict

    """
    btnext = "press SPACE" if device == "keyboard" else "click the mouse"
    texts = {
        "done": "You have completed the task. Thank you for your participation.",
        "slower": "Slower",
        "faster": "Faster",
        "checkOximeter": "Please make sure the oximeter is correctly clipped to your finger.",
        "stayStill": "Please stay still during the recording",
        "tooLate": "Too late",
        "correctResponse": "Correct",
        "incorrectResponse": "False",
        "VASlabels": ["Guess", "Certain"],
        "textHeartListening": "Listen to your heart",
        "textToneListening": "Listen to the tones",
        "textTaskStart": "The task is now going to start, get ready.",
        "textBreaks": f"Break. You can rest as long as you want. Just {btnext} when you want to resume the task.",
        "textNext": f"Please {btnext} to continue",
        "textWaitTrigger": "Waiting for fMRI trigger...",
        "Decision": {
            "Intero": """Are these beeps faster or slower than your heart?""",
            "Extero": """Are these beeps faster or slower than the previous?""",
        },
        "Confidence": """How confident are you in your choice?""",
    }

    if device == "keyboard":
        texts["responseText"] = "Use DOWN key for slower - UP key for faster."
    elif device == "mouse":
        texts["responseText"] = "Use LEFT button for slower - RIGHT button for faster."

    texts[
        "Tutorial1"
    ] = """During this experiment, we will record your pulse and play beeps based on your heart rate.

You will only be allowed to focus on the internal sensations of your heartbeats, but not to measure your heart rate by any other means (e.g. checking pulse at your wrist or your neck).
        """
    texts[
        "pulseTutorial1"
    ] = "Please place the pulse oximeter on your forefinger. Use your non-dominant hand as depicted in this schema."

    texts[
        "pulseTutorial2"
    ] = "If you can feel your heartbeats when you have the pulse oximeter on your forefinger, try to place it on another finger."

    texts[
        "pulseTutorial3"
    ] = "You can test different configurations until you find the finger which provides you with the least sensory input about your heart rate."

    texts[
        "pulseTutorial4"
    ] = "Please enter the number of the finger corresponding to the finger where you decided to place the pulse oximeter."

    texts[
        "Tutorial2"
    ] = "When you see this icon, try to focus on your heartbeat for 5 seconds. Try not to move, as we are recording your pulse in this period"

    moreResp = "UP key" if device == "keyboard" else "RIGHT mouse button"
    lessResp = "DOWN key" if device == "keyboard" else "LEFT mouse button"
    texts[
        "Tutorial3_icon"
    ] = """After this 'heart listening' period, you will see the same icon and hear a series of beeps."""
    texts[
        "Tutorial3_responses"
    ] = f"""As quickly and accurately as possible, you will listen to these beeps and decide if they are faster ({moreResp}) or slower ({lessResp}) than your own heart rate.

The beeps will ALWAYS be slower or faster than your heart. Please guess, even if you are unsure."""

    if exteroception is True:
        texts[
            "Tutorial3bis"
        ] = """For some trials, instead of seeing the heart icon, you will see a listening icon. You will then have to listen to a first set of beeps, instead of your heart."""

        texts[
            "Tutorial3ter"
        ] = f"""After these first beeps, you will see the response icons appear, and a second set of beeps will play.

As quickly and accurately as possible, you will listen to these beeps and decide if they are faster ({moreResp}) or slower ({lessResp}) than the first set of beeps.

The second series of beeps will ALWAYS be slower or faster than the first series. Please guess, even if you are unsure."""

    texts[
        "Tutorial4"
    ] = """Once you have provided your decision, you will also be asked to rate how confident you feel in your decision.

Here, the maximum rating (100) means that you are totally certain in your choice, and the smallest rating (0) means that you felt that you were guessing.

You should use mouse to select your rating"""

    texts[
        "Tutorial5"
    ] = """This sequence will be repeated during the task.

At times the task may be very difficult; the difference between your true heart rate and the presented beeps may be very small.

This means that you should try to use the entire length of the confidence scale to reflect your subjective uncertainty on each trial.

As the task difficulty will change over time, it is rare that you will be totally confident or totally uncertain."""

    texts[
        "Tutorial6"
    ] = """This concludes the tutorial. If you have any questions, please ask the experimenter now.
Otherwise, you can continue to the main task."""

    return texts


def danish(device: str, setup: str, exteroception: bool) -> Dict[str, Collection[str]]:
    """Create the text dictionary with instruction in Danish

    Parameters
    ----------
    device : str
        Can be `"keyboard"` or `"mouse"`.
    setup : str
        The experimental setup. Can be `"behavioral"` or `"test"`.
    exteroception : bool
        If `True`, the task includes and exteroceptive control condition.

    Returns
    -------
    texts : dict

    """

    btnext = "tryk på mellemrumstasten" if device == "keyboard" else "klik på musen"
    texts = {
        "done": "Du har genemført opgaven. Tak for din deltagalse.",
        "slower": "Langsommere",
        "faster": "Hurtigere",
        "checkOximeter": "Sørg venligst for at pulsoximeteret sidder rigtigt på din finger.",
        "stayStill": "Sid venligst roligt under målingen",
        "tooLate": "For langsomt",
        "correctResponse": "Rigtigt",
        "incorrectResponse": "Forkert",
        "VASlabels": ["Gæt", "Helt sikker"],
        "textHeartListening": "Mærk din hjerterytme",
        "textToneListening": "Lyt til tonerne",
        "textTaskStart": "Opgaven begynder nu, gør dig klar.",
        "textBreaks": f"Pause. Du kan tage så lang en pause, som du har brug for. Bare {btnext} når du vil fortsætte opgaven.",
        "textNext": f"Venligst, {btnext} for at fortsætte",
        "textWaitTrigger": "Venter på fMRI-udløseren...",
        "Decision": {
            "Intero": """Er disse bib-lyde hurtigere eller langsommere end dit hjerte?""",
            "Extero": """Er disse bib-lyde hurtigere eller langsommere end den de forrige? """,
        },
        "Confidence": """Hvor sikker er du på dit svar?""",
    }

    if device == "keyboard":
        texts[
            "responseText"
        ] = "Brug NED tasten for langsommere - OP tasten for hurtigere."
    elif device == "mouse":
        texts[
            "responseText"
        ] = "Brug VENSTRE museknap for langsommere - HØJRE museknap for hurtigere."

    texts[
        "Tutorial1"
    ] = """I dette forsøg vil vi registrere din puls og afspille bib-lyde baseret på din hjerterytme.

Du må kun fokusere på din indre følelse af din hjerterytme. Du må altså ikke måle din hjerterytme på andre måder (fx ved at tjekke din puls på dit håndled eller din hals).
        """
    texts[
        "pulseTutorial1"
    ] = "Placer venligst puls oximeteret på din pegefinger. Brug din ikke-dominante hånd som beskrevet i dette skema."

    texts[
        "pulseTutorial2"
    ] = "Hvis du kan mærke din hjerterytme, når du har puls oximeteret på din pegefinger, så prøv at placere det på en anden finger."

    texts[
        "pulseTutorial3"
    ] = "Du kan teste forskellige fingre indtil du finder den finger, der giver dig mindst sensorisk indput omkring din hjerterytme."

    texts[
        "pulseTutorial4"
    ] = "Indtast venligt nummeret på den finger som du besluttede at placere puls oximeteret på."

    texts[
        "Tutorial2"
    ] = "Når du ser dette ikon, forsøg da at fokusere på din hjerterytme i 5 sekunder. Prøv ikke at bevæge dig, da vi registrere din puls i dette tidsrum"

    moreResp = "OP tasten" if device == "keyboard" else "HØJRE mussetast"
    lessResp = "NED tasten" if device == "keyboard" else "VENSTRE mussetast"
    texts[
        "Tutorial3_icon"
    ] = """Efter tidsrummet hvor du har forsøgt at mærke dit hjerte, vil du se det samme ikon og høre en række bib-lyde."""
    texts[
        "Tutorial3_responses"
    ] = f"""Det følgende skal du gøre så hurtigt og præcist som muligt: Du vil lytte til disse bib-lyde og beslutte om de er hurtigere ({moreResp}) eller langsommere ({lessResp}) end din egen hjerterytme.

Bib-lydene vil ALTID være langsommere eller hurtigere end dit hjerte. Gæt venligst selvom du er usikker."""

    if exteroception is True:
        texts[
            "Tutorial3bis"
        ] = """I nogle runder vil du se et lytteikon i stedet for et hjerteikon. Her vil du skulle lytte til et sæt af bib-lyde i stedet for dit hjerte."""

        texts[
            "Tutorial3ter"
        ] = f"""Efter dette sæt af bib-lyde vil du se, at svarikonet dukker op, og et andet sæt af bib-lyde vil blive afspillet.

Det følgende skal du gøre så hurtigt og præcist som muligt: Du vil lytte til det sidste sæt af bib-lyde og beslutte om de er hurtigere ({moreResp}) eller langsommere ({lessResp}) end det første sæt af bib-lyde.

Det andet sæt af bib-lyde vil ALTID være langsommere eller hurtigere end det første sæt. Gæt venligst selvom du er usikker."""

    texts[
        "Tutorial4"
    ] = """Når du har svaret, vil du også blive bedt om at angive hvor sikker du er på din beslutning.

Her betyder den højeste score (100) at du er helt sikker på dit valg, og den mindste score (0) betyder, at du følte, at du gættede.

Du skal bruge musen til at vælge en score."""

    texts[
        "Tutorial5"
    ] = """Denne sekvens vil blive gentaget igennem opgaven.

Nogle gange kan opgaven være virkelig svær; forskellen mellem din faktiske hjerterytme og bib-lydene kan være meget små.

Dette betyder, at du skal forsøge at bruge hele skalaens længde til at angive din subjektive usikkerhed i hver runde.

Da opgavens sværhedsgrad ændrer sig over tid, er det sjældent at du vil være totalt sikker eller totalt usikker."""

    texts[
        "Tutorial6"
    ] = """Dette er slutningen på vejledningen. Hvis du har noget spørgsmål, så spørg endelig en forsker nu.
Ellers kan du fortsætte til hovedopgaven."""

    return texts


def danish_children(
    device: str, setup: str, exteroception: bool
) -> Dict[str, Collection[str]]:
    """Create the text dictionary with instruction in Danish (simplified version for
    children).

    Parameters
    ----------
    device : str
        Can be `"keyboard"` or `"mouse"`.
    setup : str
        The experimental setup. Can be `"behavioral"` or `"test"`.
    exteroception : bool
        If `True`, the task includes and exteroceptive control condition.

    Returns
    -------
    texts : dict

    """

    btnext = "tryk på mellemrumstasten" if device == "keyboard" else "klik på musen"
    texts = {
        "done": "Du har genemført opgaven. Tak for din deltagalse.",
        "slower": "Langsommere",
        "faster": "Hurtigere",
        "checkOximeter": "Spørg forskningsassistensen om, hvordan du skal placere fingerklemmen.",
        "stayStill": "Sid venligst roligt under målingen",
        "tooLate": "For langsomt",
        "correctResponse": "Rigtigt",
        "incorrectResponse": "Forkert",
        "VASlabels": ["Slet ikke sikker", "Helt sikker"],
        "textHeartListening": "Mærk din indre puls",
        "textToneListening": "Lyt til tonerne",
        "textTaskStart": "Opgaven begynder nu, gør dig klar.",
        "textBreaks": f"Pause. Du kan tage så lang en pause, som du har brug for. Bare {btnext} når du vil fortsætte opgaven.",
        "textNext": f"Venligst, {btnext} for at fortsætte",
        "textWaitTrigger": "Venter på fMRI-udløseren...",
        "Decision": {
            "Intero": """Er disse bib-lyde hurtigere eller langsommere end dit hjerte?""",
            "Extero": """Er disse bib-lyde hurtigere eller langsommere end den de forrige? """,
        },
        "Confidence": """Hvor sikker er du på dit svar?""",
    }

    if device == "keyboard":
        texts[
            "responseText"
        ] = "Brug NED tasten for langsommere - OP tasten for hurtigere."
    elif device == "mouse":
        texts[
            "responseText"
        ] = "Brug VENSTRE museknap for langsommere - HØJRE museknap for hurtigere."

    texts[
        "Tutorial1"
    ] = """Instruktion 1
        """
    texts["pulseTutorial1"] = "Udstyr."

    texts["pulseTutorial2"] = ""

    texts["pulseTutorial3"] = ""

    texts[
        "pulseTutorial4"
    ] = "Indtast venligt nummeret på den finger som du besluttede at placere fingerklemmen på."

    texts[
        "Tutorial2"
    ] = "Når du ser dette ikon, forsøg da at fokusere på din indre puls i 5 sekunder. Prøv ikke at bevæge dig, da vi måler din puls i dette tidsrum"

    moreResp = "OP tasten" if device == "keyboard" else "HØJRE mussetast"
    lessResp = "NED tasten" if device == "keyboard" else "VENSTRE mussetast"
    texts[
        "Tutorial3_icon"
    ] = """Efter du har forsøgt at mærke din indre puls, vil du se det samme ikon og høre en række bib-lyde."""
    texts["Tutorial3_responses"] = """Instruktion 2"""

    if exteroception is True:
        texts[
            "Tutorial3bis"
        ] = """I nogle runder vil du se et lytteikon i stedet for et hjerteikon. Her vil du skulle lytte til et sæt af bib-lyde i stedet for dit hjerte."""

        texts[
            "Tutorial3ter"
        ] = f"""Efter dette sæt af bib-lyde vil du se, at svarikonet dukker op, og et andet sæt af bib-lyde vil blive afspillet.

Det følgende skal du gøre så hurtigt og præcist som muligt: Du vil lytte til det sidste sæt af bib-lyde og beslutte om de er hurtigere ({moreResp}) eller langsommere ({lessResp}) end det første sæt af bib-lyde.

Det andet sæt af bib-lyde vil ALTID være langsommere eller hurtigere end det første sæt. Gæt venligst selvom du er usikker."""

    texts["Tutorial4"] = """Instruktion 3"""

    texts["Tutorial5"] = """Instruktion 4"""

    texts[
        "Tutorial6"
    ] = """Dette er slutningen på vejledningen. Hvis du har noget spørgsmål, så spørg endelig en forsker nu.
Ellers kan du fortsætte til opgaven."""

    return texts


def french(device: str, setup: str, exteroception: bool) -> Dict[str, Collection[str]]:
    """Create the text dictionary with instruction in french

    Parameters
    ----------
    device : str
        Can be `"keyboard"` or `"mouse"`.
    setup : str
        The experimental setup. Can be `"behavioral"` or `"test"`.
    exteroception : bool
        If `True`, the task includes and exteroceptive control condition.

    Returns
    -------
    texts : dict

    """
    btnext = (
        "appuyez sur la barre espace"
        if device == "keyboard"
        else "cliquez sur la souris"
    )
    texts = {
        "done": "Vous avez terminé la tâche. Merci pour votre participation.",
        "slower": "Plus lent",
        "faster": "Plus rapide",
        "checkOximeter": "Assurez-vous que l'oxymètre est bien attaché à votre doigt.",
        "stayStill": "Veuillez ne pas bouger pendant l'enregistrement",
        "tooLate": "Trop tard",
        "correctResponse": "Correct",
        "incorrectResponse": "Faux",
        "VASlabels": ["Incertain", "Tout à fait sûr"],
        "textHeartListening": "Ecoutez votre coeur",
        "textToneListening": "Ecoutez les sons",
        "textTaskStart": "La tâche va débuter, tenez-vous prêt.",
        "textBreaks": f"Pause. Vous pouvez vous reposer aussi longtemps que vous le souhaitez. Simplement {btnext} quand vous désirez rependre la tâche.",
        "textNext": f"S'il vous plaît {btnext} pour continuer",
        "textWaitTrigger": "Attendez pour le déclencheur IRMf...",
        "Decision": {
            "Intero": """Est-ce que ces sons sont plus rapides ou plus lents que votre coeur?""",
            "Extero": """Est-ce que ces sons sont plus rapides ou plus lents que les précédents?""",
        },
        "Confidence": """Etes-vous sûr de votre choix?""",
    }

    if device == "keyboard":
        texts[
            "responseText"
        ] = "Appuyez sur la flèche vers le BAS pour plus lent - vers le HAUT pour plus rapide."
    elif device == "mouse":
        texts[
            "responseText"
        ] = "Appuyez sur le clic GAUCHE pour plus lent - clic DROIT pour plus rapide."

    texts[
        "Tutorial1"
    ] = """Durant cette tâche, nous allons enregistrer vos pulsations et jouer des sons basés sur votre rythme cardiaque.

Vous serez uniquement autorisés à vous concentrer sur vos sensations internes de vos battements cardiaques, mais ne mesurez pas votre rythme cardiaque par d'autres moyens (ex. vérification du pouls au poignet ou au cou).
        """
    texts[
        "pulseTutorial1"
    ] = "Veuillez placer l'oxymètre de pouls sur votre index. Utilisez votre main non-dominante comme illustré sur ce schéma."

    texts[
        "pulseTutorial2"
    ] = "Si vous pouvez sentir vos battements de coeur quand vous portez l'oxymètre de pouls sur votre index, essayez de le placer sur un autre doigt."

    texts[
        "pulseTutorial3"
    ] = "Vous pouvez essayer différentes configurations jusqu'à ce que vous trouviez le doigt qui provoque le moins de sensations de battements cardiaques."

    texts[
        "pulseTutorial4"
    ] = "Veuillez entrer le numéro du doigt correspondant au doigt sur lequel vous avez décidé de placer l'oxymètre de pouls."

    texts[
        "Tutorial2"
    ] = "Quand vous voyez cette icône, essayez de vous concentrer sur vos battements cardiaques durant 5 secondes. Essayez de ne pas bouger, car nous enregistrons votre pouls durant cette période."

    moreResp = "flèche vers le HAUT" if device == "keyboard" else "clic DROIT"
    lessResp = "flèche vers le BAS" if device == "keyboard" else "clic GAUCHE"
    texts[
        "Tutorial3_icon"
    ] = """Après cette période d'écoute du coeur, vous verrez la même icône and entendrez une série de bips."""
    texts[
        "Tutorial3_responses"
    ] = f"""Aussi rapidement et précisément possible, vous écouterez ces bips et déciderez s'ils sont plus rapides ({moreResp}) ou plus lents ({lessResp}) que votre propre rythme cardiaque.

Les bips seront TOUJOURS plus lents ou plus rapides que votre coeur. Veuillez faire une estimation, même si vous n'est pas sûr."""

    if exteroception is True:
        texts[
            "Tutorial3bis"
        ] = """Pour certains essais, au lieu de voir une icône de coeur, vous verrez une icône d'écoute. Vous devrez alors écouter une première série de bips, au lieu de votre coeur."""

        texts[
            "Tutorial3ter"
        ] = f"""Après ce premier bip, vous verrez l'icône de réponse apparaître, et une seconde série de bip sera joué.

Aussi rapidement et précisément possible, vous entendrez ces bips et déciderez s'ils sont plus rapides ({moreResp}) ou plus lents ({lessResp}) que la première série de bips.

La seconde série de bips sera TOUJOURS plus lente ou rapide que la première série. Veuillez faire une estimation, même si vous n'êtes pas sûr."""

    texts[
        "Tutorial4"
    ] = """Une fois que vous avez donné votre réponse, il vous sera également demandé d'estimer votre degré de confiance dans votre réponse.

Ici, le score maximum (100) signifie que vous êtes totalement certain de votre choix, et le score minimum (0) signifie que vous devinez.

Vous devez utiliser la souris pour sélectionner votre score"""

    texts[
        "Tutorial5"
    ] = """Cette séquence sera répétée durant la tâche.

Par moment la tâche peut être très difficile ; la différence entre votre propre rythme cardiaque et les bips présentés peut être très petite.

Cela signifie que vous devez essayer d'utiliser toute la longueur de l'échelle de confiance pour refléter votre incertitude subjective sur chaque essai.

Comme la difficulté de la tâche évolue avec le temps, il est rare que vous soyez totalement confiant ou totalement incertain."""

    texts[
        "Tutorial6"
    ] = """Ceci conclut le tutoriel. Si vous avez des questions, veuillez les poser maintenant à l'expérimentateur.
Sinon, vous pouvez continuer avec la tâche principale."""

    return texts

def korean(device: str, setup: str, exteroception: bool) -> Dict[str, Collection[str]]:
    """Create the text dictionary with instruction in Korean

    Parameters
    ----------
    device : str
        Can be `"keyboard"` or `"mouse"`.
    setup : str
        The experimental setup. Can be `"behavioral"` or `"test"`.
    exteroception : bool
        If `True`, the task includes and exteroceptive control condition.

    Returns
    -------
    texts : dict

    """
    btnext = "스페이스를 누르세요" if device == "keyboard" else "마우스를 클릭하세요"
    texts = {
        "done": "과제를 완료했습니다. 참여해 주셔서 감사합니다.",
        "slower": "느리게",
        "faster": "빠르게",
        "checkOximeter": "센서가 손가락에 올바르게 끼워졌는지 확인해 주십시오.",
        "stayStill": "기록 중에는 가만히 있어 주십시오.",
        "tooLate": "너무 늦었습니다.",
        "correctResponse": "맞음",
        "incorrectResponse": "틀림",
        "VASlabels": ["추측", "확실"],
        "textHeartListening": "당신의 심장에 귀기울여 보십시오.",
        "textToneListening": "소리에 귀기울여 보십시오.",
        "textTaskStart": "이제 과제가 시작됩니다. 준비하십시오.",
        "textBreaks": f"쉬는 시간입니다. 원하는 만큼 쉴 수 있습니다. 과제를 다시 시작하려면 {btnext}.",
        "textNext": f"계속하려면 {btnext}",
        "textWaitTrigger": "fMRI 트리거를 기다리는 중 ...",
        "Decision": {
            "Intero": """삐 소리들이 당신의 심장보다 빠릅니까? 아니면 느립니까?""",
            "Extero": """삐 소리들이 이전 것보다 빠릅니까? 아니면 느립니까?""",
        },
        "Confidence": """당신의 선택에 얼마나 자신이 있습니까?""",
    }

    if device == "keyboard":
        texts["responseText"] = "느리게 하려면 아래 방향 키를 사용하고, 빠르게 하려면 위 방향 키를 사용하십시오."
    elif device == "mouse":
        texts["responseText"] = "느리게 하려면 마우스 왼쪽 버튼을 사용하고, 빠르게 하려면 마우스 오른쪽 버튼을 사용하십시오."

    texts[
        "Tutorial1"
    ] = """실험 동안 당신의 맥박을 기록하고, 심박수에 따라 삐 소리를 재생합니다.

당신은 심장 박동의 내부 감각에만 집중할 수 있으며, 손목이나 목에서 맥박을 확인하는 등의 다른 방법으로 심박수를 측정해서는 안됩니다.
        """
    texts[
        "pulseTutorial1"
    ] = "집게손가락에 센서를 착용하십시오. 평소 주로 사용하지 않는 손을 사용하십시오."

    texts[
        "pulseTutorial2"
    ] = "집게손가락에 센서가 있을 때 심장 박동이 느껴지면, 다른 손가락에 착용하십시오.""

    texts[
        "pulseTutorial3"
    ] = "심박수가 가장 적게 느껴지는 손가락을 찾을 때까지 다른 손가락에 착용해 시험하십시오."

    texts[
        "pulseTutorial4"
    ] = "센서를 착용하기로 한 손가락에 해당하는 번호를 입력하십시오."

    texts[
        "Tutorial2"
    ] = "이 아이콘이 보이면 5초 동안 심장 박동에 주의를 집중하십시오. 이 기간 동안 맥박을 기록하고 있으므로 움직이지 마십시오."

    moreResp = "위 방향 키" if device == "keyboard" else "마우스 오른쪽 버튼"
    lessResp = "아래 방향 키" if device == "keyboard" else "마우스 왼쪽 버튼"
    texts[
        "Tutorial3_icon"
    ] = """심장 박동에 귀 기울이는 기간이 끝나면, 같은 아이콘이 표시되고 삐- 소리들을 듣게 됩니다."""
    texts[
        "Tutorial3_responses"
    ] = f"""삐- 소리를 듣고 가능한 한 빠르고 정확하게, 삐 소리가 자신의 심박수보다 빠른지 ({moreResp}) 느린지 ({lessResp}) 결정합니다.

삐 소리는 항상 심장 박동보다 느리거나 빠릅니다. 잘 모르겠어도 둘 중 하나를 선택하십시오."""

    if exteroception is True:
        texts[
            "Tutorial3bis"
        ] = """일부 시행에서는 하트 아이콘 대신 듣기 아이콘이 표시됩니다. 이 때는 당신의 심장이 아니라, 삐 소리들에 귀 기울여야 합니다."""

        texts[
            "Tutorial3ter"
        ] = f"""삐 소리들이 들리고 난 후, 응답 아이콘이 나타나고 두 번째 삐 소리들을 듣게 됩니다.

두 번째 삐 소리들을 들은 다음, 이 소리들이 첫 번째 삐 소리들보다 빠른지 ({moreResp}) 혹은 느린지 ({lessResp}) 가능한 한 빠르고 정확하게 응답하십시오.

두 번째 삐 소리들은 항상 첫 번째 삐 소리들보다 느리거나 빠릅니다. 잘 모르겠어도 둘 중 하나를 선택하십시오."""

    texts[
        "Tutorial4"
    ] = """응답하고 나면, 당신의 응답에 얼마나 자신이 있는지 평가하게 됩니다.

여기서 최대 (100)은 선택에 대해 전적으로 확신한다는 것을 의미하고 가장 낮은 등급(0)은 추측하고 있다고 느꼈다는 것을 의미합니다.

마우스를 이용해 응답해 주십시오."""

    texts[
        "Tutorial5"
    ] = """이러한 순서는 시행 마다 반복됩니다.

때때로 과제가 매우 어려울 수 있습니다. 실제 심박수와 표시된 경고음 간의 차이는 매우 작을 수 있습니다.

따라서, 당신은 자신의 응답에 대한 확신을 평가할 때, 전체 척도 범위 (0에서 100까지)를 사용해야 합니다.

과제 난이도는 시간이 지남에 따라 변하기 때문에 완전히 자신감이 있거나 완전히 불확실한 경우는 드뭅니다."""

    texts[
        "Tutorial6"
    ] = """설명을 마치겠습니다. 궁금한 점이 있으면 지금 실험자에게 물어보십시오.
그렇지 않으면, 본 시행을 시작할 수 있습니다."""

    return texts
