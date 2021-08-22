darkThemeCss = document.getElementById('dark-theme');
const savedTheme = localStorage.getItem(THEME_PREF_STORAGE_KEY) || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
const darkThemeToggles = document.querySelectorAll('.dark-theme-toggle');
setTheme(savedTheme, darkThemeToggles);
darkThemeToggles.forEach((el) =>
    el.addEventListener('click', (event) => {
        toggleIcon = event.currentTarget.querySelector('a svg.feather');
        if (toggleIcon.classList[1] === THEME_TO_ICON_CLASS.dark) {
            setTheme('light', [event.currentTarget]);
        } else if (toggleIcon.classList[1] === THEME_TO_ICON_CLASS.light) {
            setTheme('dark', [event.currentTarget]);
        }
    })
);