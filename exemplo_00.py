from loguru import logger

logger.add("meu_app.log", level="CRITICAL")

def soma(x, y):
    try:
        soma = x + y
        logger.info(f"Voce digitou valores corretor {soma}")
        return soma
    except:
        logger.critical("Voce tem que digitar valores corretor")

soma(2,"3")

soma(2, 8)