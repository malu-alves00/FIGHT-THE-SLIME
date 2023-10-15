import pygame

items = {
    # item_id: [unique_id, "name", value, "description", "image"]
    0: [0, "craft", "Gosma verde", 4, "A gosma mais verde do jogo", "imagens/criacao/gosmaverde.png"],
    1: [1, "craft","Olho maldoso", 5, "Ele te olha com más intenções...", "imagens/criacao/olhomaldoso.png"],
}

weapons = {
    # item_id: [unique_id, "name", value, "description", damage, "image", optional-effects]
    0: [2, "weapon", "Faca velha podre", 8, "Cuidado para não pegar tétano", 8, "imagens/armas/facavelha.png"]
}

consumables = {
    # item_id: [unique_id, "name", value, "description", "effects" or ["effect1","effect2"], amount or [amount1,amount2], "imagem"]
    0: [3, "consumable", "Raiz fedida", 4 , "Talvez comer seja uma boa ideia?", "cura", 10, "imagens/usavel/raizfedida.png"]
}