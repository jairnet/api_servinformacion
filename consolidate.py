import pandas as pd


def consolidate_data(register):
    read_excel = pd.read_excel('election_results.xlsx')
    if register in read_excel.columns:
        group = read_excel.groupby(register, sort=False)['votos'].sum().reset_index()
        group.to_excel(f'{register}.xlsx', index=False)
        print(f'::: Se creo exitosamente el archivo {register}.xlsx :::')
    else:
        raise Exception(f'Columna | {register} | no encontrada en el archivo excel.')


def main():
    consolidate_data('candidato')
    # consolidate_data('partido')
    # consolidate_data('puesto')
    # consolidate_data('mpio')
    # consolidate_data('dept')


if __name__ == "__main__":
    main()
