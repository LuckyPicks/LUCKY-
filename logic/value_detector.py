def find_value_props(props):

    value_props = []

    for prop in props:
        try:
            projection = prop.get("projection", 0)
            line = prop.get("line", 0)

            edge = projection - line

            if edge > 1:
                prop["edge"] = edge
                value_props.append(prop)

        except:
            continue

    return value_props