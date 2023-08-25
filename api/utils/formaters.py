def format_cpf(unformated_cpf: str) -> str:
    if len(unformated_cpf) == 11:
        return f"{unformated_cpf[:3]}.{unformated_cpf[3:6]}.{unformated_cpf[6:9]}-{unformated_cpf[9:]}"
    else:
        raise ValueError
