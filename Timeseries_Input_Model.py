# Many repetitions of sounds
# In this exercise, you'll start with perhaps the simplest classification technique: averaging across dimensions of a dataset and visually
# inspecting the result.
# You'll use the heartbeat data described in the last chapter. Some recordings are normal heartbeat activity, while others are abnormal 
# activity. Let's see if you can spot the difference.

fig, axs = plt.subplots(3, 2, figsize=(15, 7), sharex=True, sharey=True)

# Calculate the time array
time = np.arange(len(normal)) / sfreq

# Stack the normal/abnormal audio so you can loop and plot
stacked_audio = np.hstack([normal, abnormal]).T

# Loop through each audio file / ax object and plot
# .T.ravel() transposes the array, then unravels it into a 1-D vector for looping
for iaudio, ax in zip(stacked_audio, axs.T.ravel()):
    ax.plot(time, iaudio)
show_plot_and_make_titles()

