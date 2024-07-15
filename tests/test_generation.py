import pytest

theorists = ["autora[theorist-darts]", "autora[theorist-bms]", "autora[theorist-bsr]"]
experimentalists = [
    "autora[experimentalist-inequality]",
    "autora[experimentalist-novelty]",
    "autora[experimentalist-nearest-value]",
    "autora[experimentalist-model-disagreement]",
    "autora[experimentalist-uncertainty]",
    "autora[experimentalist-leverage]",
    "autora[experimentalist-falsification]",
    "autora[experimentalist-mixture]",
    "autora[experimentalist-prediction-filter]",
]
firebase = [False, True]
project_type = [
    "Blank",
    "HTML Button",
    "Reaction Time",
    "Multi Choice Survey",
    "Multi Select Survey",
    "Save trial parameters",
    "Lexical decision",
    "Pause/Unpause",
    "Canvas Slider Response",
    "JsPsych - Stroop",
    "JsPsych - RDK",
    "SweetBean",
    "SuperExperiment",
]


@pytest.mark.parametrize("theorist", theorists)
@pytest.mark.parametrize("experimentalist", experimentalists)
@pytest.mark.parametrize("firebase", firebase)
@pytest.mark.parametrize("p_type", project_type)
def test_requirements(copie, theorist, experimentalist, firebase, p_type):
    """Test that requirements file has necessary dependencies

    Args:
        copie (_type_): _description_
        theorist (_type_): _description_
        experimentalist (_type_): _description_
        firebase (_type_): _description_
        p_type (_type_): _description_
    """
    result = copie.copy(
        extra_answers={
            "project_name": "test",
            "theorists": theorist,
            "experimentalists": experimentalist,
            "firebase": firebase,
            "project_type": p_type,
        }
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()

    assert (
        result.project_dir / "experiment" / "research_hub" / "requirements.txt"
    ).is_file()

    with open(
        result.project_dir / "experiment/research_hub/requirements.txt", "r"
    ) as req_file:
        reqs = req_file.read()
        reqs_list = reqs.split("\n")

        assert theorist in reqs_list
        assert experimentalist in reqs_list
