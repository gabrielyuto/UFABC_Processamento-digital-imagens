import skimage as ski

image = ski.data.coins()
edges = ski.filters.sobel(image)
ski.io.imshow(edges)
ski.io.show()