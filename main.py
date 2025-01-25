from pipeline import extract,transform,load


def run_pipiline():
    source_data = extract()
    cleaned_data = transform(source_data)
    load(cleaned_data)
    





if __name__ == '__main__':
    run_pipiline()
        