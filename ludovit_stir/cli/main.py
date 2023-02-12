"""
Implementation of the ludovit_stir command line interface.
"""

import logging
import os

import typer
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from ludovit_stir.months import (
    check_for_months,
    translate_czech_to_slovak_months,
    translate_slovak_to_czech_months,
)

app = typer.Typer()


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start_bot(update: Update, context) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def translate(update: Update, context) -> None:
    """Echo the user message."""
    sk_months, cz_months = check_for_months(update.message.text)

    if sk_months:
        await update.message.reply_text(
            translate_slovak_to_czech_months(update.message.text, sk_months)
        )

    if cz_months:
        await update.message.reply_text(
            translate_czech_to_slovak_months(update.message.text, cz_months)
        )


@app.command(help="Run bot")
def start() -> None:
    """
    Starts the bot.
    """

    token = os.getenv("TELEGRAM_BOT_TOKEN", "")

    application = Application.builder().token(token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start_bot))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()
