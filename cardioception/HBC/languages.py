#-*- coding:utf-8 -*-

# Korean version : June Kang <june.kang@empathy-research.org>

from typing import Collection, Dict

def english() -> Dict[str, Collection[str]]:
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

    texts = dict()
    texts["Rest"] = "Please sit quietly until the next session"
    texts["Count"] = """After you hear START, try to count your heartbeats
        by concentrating on your body feelings.
        Stop counting when you hear STOP"""
    texts["Training"] = """After you hear START, try to count your heartbeats
        by concentrating on your body feelings
        Stop counting when you hear STOP"""
    texts["nCount"] = """How many heartbeats did you count?
        Write a number and press ENTER to validate."""
    texts["confidence"] = """
        How confident are you about your count?
        Use the RIGHT/LEFT keys to select and the DOWN key to confirm"""

    # Tutorial instructions
    texts["Tutorial1"] = """During this experiment, we will ask you to silently
        count your heartbeats for different intervals of time."""

    texts["Tutorial2"] = """
        When you see this "heart" icon, you will silently count your'
        heartbeats by focusing on your body sensations."""

    texts["Tutorial3"] = """Sometime, you will also encounter this "rest" icon.'
        In this case your task will just be to sit quietly until the next session."""

    texts["Tutorial4"] = """The beginning and the end of the task will be signalled when you hear
        the words 'START'' and 'STOP'. While counting your heartbeats, you
        may close your eyes if you find that helpful. Please keep your hand
        still during the counting period, to avoid interfering with
        the heartbeat recording."""

    texts["Tutorial5"] = """After the counting part of the task, you will be asked to report the
        exact number of heartbeats you felt during the interval between
        'START' and 'STOP'. Please do not try to estimate the number of
        heartbeats, but instead only report the heartbeats you actually felt
        during the interval. You will input your response using the number
        pad and press return when done. You can also correct your response
        using backspace."""

    texts["Tutorial6"] = """Once you have made your response, you will estimate your subjective
        feeling of confidence in how accurate your count was
        for that interval. A large number here means that you are totally
        certain you counted the exact number of heartbeats that occured,
        and a small number means that you are totally uncertain or felt that
        you were guessing about the
        number of heartbeats. You should use the RIGHT and LEFT
        key to select your response and the DOWN key to confirm."""

    texts["Tutorial7"] = """Before the main task begins there is a short resting period of
        several minutes, during which we will calibrate the heartbeat
        recording. During this period, please sit quietly with your
        hands still to avoid interfering with the calibration.
        Afterwards, the counting task will begin, and will take about
        6 minutes in total."""

    texts["Tutorial8"] = """You will now complete a short practice task.
        Please ask the experimenter if you have any questions before
        continuing to the main experiment."""

    texts["Tutorial9"] = """Good job! If you have any question, ask the experimenter now,
        otherwise press SPACE to continue to the experiment."""

    return texts


def korean() -> Dict[str, Collection[str]]:
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

    texts = dict()
    texts["Rest"] = "다음 세션까지 가만히 앉아 계십시오."
    texts["Count"] = """시작 소리를 들은 후 몸의 느낌에 집중하여 심박수를 세어 보십시오.
        그만 소리가 들리면 세기를 멈추십시오."""
    texts["Training"] = """시작 소리를 들은 후 몸의 느낌에 집중하여 심박수를 세어 보십시오.
        그만 소리가 들리면 세기를 멈추십시오."""
    texts["nCount"] = """심장이 몇 번 뛰었나요?
        숫자를 쓰고 엔터 키를 누르십시오."""
    texts["confidence"] = """당신이 센 심박수를 얼마나 확신하십니까?
        오른쪽/왼쪽 키를 사용하여 선택하고 아래 방향 키를 눌러 입력을 마치십시오."""

    # Tutorial instructions
    texts["Tutorial1"] = """이 실험동안, 당신은 다양한 간격의 시간 동안
        당신의 심장이 몇 번 뛰는지 세어보게 됩니다."""

    texts["Tutorial2"] = """이 하트 아이콘이 보이면, 몸의 감각에 주의를 기울여
        가만히 당신의 심장이 몇 번 뛰는지 세어 보십시오."""

    texts["Tutorial3"] = """때때로 이 휴식 아이콘을 보게 됩니다.
        휴식 아이콘이 보이면 다음 세션까지 가만히 앉아 있으면 됩니다."""

    texts["Tutorial4"] = """시작과 그만 소리가 과제의 시작과 끝을 알려줍니다.
        심장이 몇 번 뛰는지 세는 동안, 도움이 된다고 느끼면, 눈을 감아도 됩니다.
        심장 박동을 세는 동안 손은 가만히 두고 움직이지 마십시오. """

    texts["Tutorial5"] = """시작과 그만 사이에 심장이 몇 번 뛰는지 센 다음, 
        정확히 몇 번 뛰었다고 느꼈는지 응답하게 됩니다. 
        심박수를 추측하려 하지 마시고, 그 기간동안 정확히 느낀 횟수를 응답해 주십시오. 
        숫자 키를 이용해 응답하시고, 완료하면 엔터키를 누르십시오. 
        틀린 숫자를 입력한 경우 백스페이스를 눌러 수정할 수 있습니다."""

    texts["Tutorial6"] = """응답을 마치면, 심박수에 대한 당신의 응답에 대해
        얼마나 확신하는지 응답하게 됩니다. 
        큰 숫자는 당신이 실제 심장이 뛴 횟수를 정확하게 세었음을 뜻합니다.
        작은 숫자는 당신의 입력이 불확실하거나, 추측에 가깝다 뜻입니다. 
        오른쪽과 왼쪽 방향키를 눌러 선택하고 아래 방향 키를 눌러 결정하면 됩니다."""

    texts["Tutorial7"] = """본 시행이 시작되기 전에 몇 분간의 짧은 휴식 시간이 있습니다.
        휴식 시간동안 심박 수 기록이 잘 되는지 확인하고 보정할 것입니다.
        휴식하는 동안 가만히 앉아 계십시오.
        보정을 방해하지 않도록 손을 움직이지 마십시오.
        휴식이 끝나고, 심박수 세기 과제가 시작됩니다. 과제는 총 약 6분정도 걸립니다."""

    texts["Tutorial8"] = """이제 짧은 연습을 하게 됩니다.
        본 실험을 계속하기 전에 궁금한 점이 있으면 실험자에게 물어보십시오."""

    texts["Tutorial9"] = """잘 하셨습니다! 궁금한 점이 있으면 지금 실험자에게 물어보십시오.
        실험을 계속하려면 스페이스바를 누르십시오."""

    return texts
