from code_comp_ex.code_execution import code_execution
import pyperclip

from pynput import keyboard as kb

keyboard = kb.Controller()


def total_character_length(strings):
    total_length = 0

    for string in strings:
        total_length += len(string)

    return total_length


def code_compilation(code_string: str) -> None:
    global run_stop_code_execution
    run_stop_code_execution = False
    try:
        code_string = code_string.strip()
        automationlist = code_string.strip().split("\n")
        variable_list = []
        automation_index = 0

        for index, code_line in enumerate(automationlist):
            if run_stop_code_execution is True:
                return f"Code execution aborted at line: {code_line}"
            if automation_index > index:
                continue

            code_line = code_line.strip()
            if code_line == "":
                pass
            elif code_line[0] == "#":
                pass
            else:
                if "SetVariable" in code_line:
                    if "Clipboard()" in code_line:
                        var_name = code_line.split("(")[1].split("=")[0].strip()
                        var_value = pyperclip.paste()
                    else:
                        var_name = code_line.split("(")[1].split("=")[0].strip()
                        var_value = (
                            code_line.split("=")[1]
                            .split(")")[0]
                            .strip()
                            .replace('"', "")
                        )

                    if var_name in [variable["var_name"] for variable in variable_list]:
                        for variable in variable_list:
                            if variable["var_name"] == var_name:
                                variable["var_value"] = var_value
                            else:
                                pass
                    else:
                        variable_list.append(
                            {"var_name": var_name, "var_value": var_value}
                        )
                elif "SetVariable" not in code_line:
                    for variable in variable_list:
                        if variable["var_name"] in " " + code_line + " ":
                            code_line = code_line.replace(
                                variable["var_name"], variable["var_value"]
                            ).strip()

                if "Loop" in code_line:
                    char_number = total_character_length(automationlist[:index])
                    loop_start = code_string.find("Loop", char_number)
                    loop_end = code_string.find("}", loop_start)
                    loop_text = code_string[loop_start : loop_end + 1]
                    loop_number = int(
                        loop_text[loop_text.find("(") + 1 : loop_text.find(")")]
                    )
                    loop_text_short = loop_text[
                        loop_text.find("{") + 1 : loop_text.find("}")
                    ].strip()

                    for i in range(loop_number):
                        if run_stop_code_execution is True:
                            return f"Code execution aborted at line: {code_line}"
                        result = code_execution(loop_text_short)
                        if result is True or run_stop_code_execution is True:
                            return f"Code execution aborted at line: {code_line}"
                    for i, _ in enumerate(automationlist[index:]):
                        if "}" in _:
                            automation_index = index + i + 1
                            break

                elif "If" in code_line and "ElseIf" not in code_line:
                    char_number = total_character_length(automationlist[:index])
                    if_start = code_string.find("If", char_number)
                    if_end = code_string.find("}", if_start)
                    if_text = code_string[if_start : if_end + 1]
                    if_condition_code = if_text[
                        if_text.find("{") + 1 : if_text.find("}")
                    ].strip()
                    if_condition = code_line[
                        code_line.find("(") + 1 : code_line.find(")")
                    ].strip()

                    for i, _ in enumerate(automationlist[index:]):
                        if "}" in _:
                            automation_index = index + i
                            break

                    if_eval_result = eval(if_condition)
                    if if_eval_result:
                        result = code_execution(if_condition_code)
                        if result is True or run_stop_code_execution is True:
                            return f"Code execution aborted at line: {code_line}"
                    elseif_eval_result = False

                elif "ElseIf" in code_line and if_eval_result is False:
                    char_number = total_character_length(automationlist[:index])
                    elseif_condition = code_line[
                        code_line.find("(") + 1 : code_line.find(")")
                    ].strip()
                    elseif_eval_result = eval(elseif_condition)
                    elseif_start = code_string.find("ElseIf", char_number)
                    elseif_end = code_string.find("}", elseif_start)
                    if elseif_eval_result:
                        elseif_text = code_string[elseif_start : elseif_end + 1]
                        else_condition_code = elseif_text[
                            elseif_text.find("{") + 1 : elseif_text.find("}")
                        ].strip()
                        result = code_execution(else_condition_code)
                        if result is True or run_stop_code_execution is True:
                            return f"Code execution aborted at line: {code_line}"

                    char_len = 0
                    for i, _ in enumerate(automationlist):
                        char_len += len(_)
                        if (char_len > (elseif_end - len(_))) and "}" in _:
                            automation_index = i
                            break
                elif "Else {" in code_line or "Else{" in code_line:
                    char_number = total_character_length(automationlist[:index])
                    else_start = code_string.find("Else {", char_number)
                    if else_start == -1:
                        else_start = code_string.find("Else{", char_number)

                    else_end = code_string.find("}", else_start)

                    if if_eval_result is False and elseif_eval_result is False:
                        else_text = code_string[else_start : else_end + 1]
                        else_condition_code = else_text[
                            else_text.find("{") + 1 : else_text.find("}")
                        ].strip()
                        result = code_execution(else_condition_code)
                        if result is True or run_stop_code_execution is True:
                            return f"Code execution aborted at line: {code_line}"

                    char_len = 0
                    for i, _ in enumerate(automationlist):
                        char_len += len(_)
                        if (char_len > (else_end - len(_))) and "}" in _:
                            automation_index = i
                            break
                elif "ExecutePytobotScript" in code_line:
                    char_number = total_character_length(automationlist[:index])
                    execute_start = code_string.find(
                        "ExecutePytobotScript", char_number
                    )
                    execute_end = code_string.find(")", execute_start)
                    execute_text = code_string[execute_start : execute_end + 1]
                    execute_path = (
                        execute_text[
                            execute_text.find("(") + 1 : execute_text.find(")")
                        ]
                        .strip()
                        .replace('"', "")
                    )
                    try:
                        with open(execute_path, "r") as f:
                            code_compilation(f.read())
                    except FileNotFoundError:
                        raise FileNotFoundError(
                            "File {} not found. Please check the path and try again.".format(
                                execute_path
                            )
                        )

                elif (
                    "SetVariable" not in code_line
                    and "Loop" not in code_line
                    and "If" not in code_line
                    and "Else" not in code_line
                ):
                    result = code_execution(code_line)
                    if result is True or run_stop_code_execution is True:
                        return f"Code execution aborted at line: {code_line}"
                    elif result is type(str):
                        raise Exception(result)

        return "Code executed successfully."

    except Exception as e:
        return "There was an error with the code. Please try again. Error: {}".format(e)
