def in_center(elementSize, surfaceSize, surfacePosition):
    x = surfacePosition[0] + (surfaceSize[0] // 2) - (elementSize[0] // 2)
    y = surfacePosition[1] + (surfaceSize[1] // 2) - (elementSize[1] // 2)
    return (x, y)
