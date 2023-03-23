import click
from colorama import just_fix_windows_console, Style, Fore

@click.command()
def setup_wizard():
  '''GPU Passthrough and KVM setup wizard, Windows XP style!'''
  just_fix_windows_console()
  click.echo(Style.BRIGHT + Fore.GREEN + "Welcome to SplitScreen-KVM, a setup wizard for GPU passthrough" + Style.RESET_ALL)
