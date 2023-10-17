def make_readable(secs):
    hrs = secs // 3600
    mnts = (secs // 60) % 60
    secns = secs - (hrs * 3600) - (mnts * 60)
    return f'{hrs:02d}:{mnts:02d}:{secns:02d}'
