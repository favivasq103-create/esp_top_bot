import discord
from discord import app_commands
TOKEN = "MTQ1Njc5ODU1NTIzODAzOTU2Mg.G6p4Iy.WEU7Hs6E4bBUN05PYSxOmqqP1xJW0JebGlFT9s"  

class DecorBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    async def setup_hook(self):
        await self.tree.sync()
        print("✅ Comandos sincronizados")
bot = DecorBot()

@bot.event
async def on_ready():
    print(f"🤖 Bot conectado como {bot.user}")

@bot.tree.command(
    name="ideas",
    description="Ideas de decoración para el hogar con materiales reciclables"
)
async def ideas(interaction: discord.Interaction):
    await interaction.response.send_message(
        "♻️ **Ideas de decoración reciclable**\n\n"
        "🕯️ Porta velas con frascos de vidrio\n"
        "🖼️ Marcos de fotos con cartón\n"
        "🌼 Macetas con botellas plásticas\n"
        "💡 Lámparas con latas\n"
        "🧺 Organizadores con cajas recicladas"
    )
@bot.tree.command(
    name="pasos",
    description="Explicación paso a paso de una decoración reciclable"
)
@app_commands.describe(objeto="Ejemplo: maceta, lámpara, marco")
async def pasos(interaction: discord.Interaction, objeto: str):
    await interaction.response.send_message(
        f"🛠️ **Cómo hacer un(a) {objeto} reciclable**\n\n"
        "1️⃣ Lava y seca los materiales\n"
        "2️⃣ Diseña el proyecto antes de empezar\n"
        "3️⃣ Usa pegamento, silicona o hilo\n"
        "4️⃣ Decora con pintura ecológica\n"
        "5️⃣ Deja secar y colócalo en tu hogar\n\n"
        "⚠️ Consejo: usa guantes si trabajas con vidrio o latas"
    )
@bot.tree.command(
    name="materiales",
    description="Materiales reciclables recomendados"
)
async def materiales(interaction: discord.Interaction):
    await interaction.response.send_message(
        "♻️ **Materiales reciclables comunes**\n\n"
        "- Botellas plásticas\n"
        "- Frascos de vidrio\n"
        "- Cartón y papel\n"
        "- Latas\n"
        "- Telas usadas\n"
        "- Madera reciclada"
    )

@bot.tree.command(
    name="nivel",
    description="Nivel de dificultad del proyecto"
)
@app_commands.describe(dificultad="fácil, medio o difícil")
async def nivel(interaction: discord.Interaction, dificultad: str):
    await interaction.response.send_message(
        f"📊 **Nivel seleccionado: {dificultad.upper()}**\n\n"
        "🟢 Fácil: proyectos simples y rápidos\n"
        "🟡 Medio: requiere herramientas básicas\n"
        "🔴 Difícil: más tiempo y precisión\n\n"
        "⏱️ Tiempo estimado: 30–120 minutos"
    )

@bot.tree.command(
    name="impacto",
    description="Beneficios ecológicos del reciclaje decorativo"
)
async def impacto(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🌍 **Impacto ecológico positivo**\n\n"
        "✅ Reduce residuos\n"
        "✅ Ahorra dinero\n"
        "✅ Reutiliza materiales\n"
        "✅ Embellece el hogar\n"
        "✅ Ayuda al medio ambiente"
    )
bot.run("MTQ1Njc5ODU1NTIzODAzOTU2Mg.G6p4Iy.WEU7Hs6E4bBUN05PYSxOmqqP1xJW0JebGlFT9s")
