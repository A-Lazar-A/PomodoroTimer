import time
import click
from art import text2art
from tqdm import tqdm


def print_green(msg):
    click.echo(click.style(msg, fg='green'))


def print_red(msg):
    click.echo(click.style(msg, fg='red'))


def main(count_pomodoro_done, time_to_work, time_to_rest, time_to_big_rest):
    bar_format = '{desc} {percentage:3.0f}%|{bar}|{remaining}'
    if count_pomodoro_done:
        print(f'You have done {count_pomodoro_done} Pomodoro!')
        time.sleep(1)
    if count_pomodoro_done % 4 == 0 and count_pomodoro_done:
        print_green('You need to do a BIG rest!')
        time.sleep(1)
        for _ in tqdm(range(time_to_big_rest), colour='green', desc='CHILL', bar_format=bar_format, ncols=50):
            time.sleep(1)

    print_red('Do some job!')
    time.sleep(1)
    for _ in tqdm(range(time_to_work), colour='red', desc='Working...', bar_format=bar_format, ncols=50):
        time.sleep(1)
    print_green('Do some rest!')
    time.sleep(1)
    for _ in tqdm(range(time_to_rest), colour='green', desc='Chilling...', bar_format=bar_format, ncols=50):
        time.sleep(1)
    count_pomodoro_done += 1

    return count_pomodoro_done


@click.command()
@click.option('--inf', is_flag=True, show_default=True, default=False, help='Set infinite mode')
@click.option('--count', default=4, show_default=True, type=int, help='Set counts of Pomodoro')
def pomodoro(count, inf):
    print(text2art('Pomodoro'))
    time_to_work = 60 * 25
    time_to_rest = 60 * 5
    time_to_big_rest = time_to_rest + time_to_work
    count_pomodoro_done = 0

    if inf:
        while True:
            count_pomodoro_done = main(count_pomodoro_done, time_to_work, time_to_rest, time_to_big_rest)

    else:
        while count != count_pomodoro_done:
            count_pomodoro_done = main(count_pomodoro_done, time_to_work, time_to_rest, time_to_big_rest)


if __name__ == '__main__':
    pomodoro()


