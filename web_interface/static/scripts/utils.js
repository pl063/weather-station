
    function getTime () {
 
        let date = new Date();

        let day = date.getDate();
        let shortMonth = date.getMonth();
        let year = date.getFullYear();
        let currentDay = `${day}/${shortMonth}/${year}`;

        let minutes = date.getMinutes();
        let displayMinutes = minutes < 10 ? `0${minutes}` : minutes
        let time = `${date.getHours()}:${displayMinutes}`;

        return {currentDay, time}
    }

    function updateImageUrl (weatherState) {
        //return object w/ background image and icon
        let result = {
            iconUrl: "",
            backgroundUrl: ""
        };

        switch (weatherState) {
            case "hot": 
                result.iconUrl = "https://res.cloudinary.com/weather-station-viper/image/upload/v1698516321/weather_icons/device_thermostat1_dukwu9.svg";
                result.backgroundUrl = "https://res.cloudinary.com/weather-station-viper/image/upload/v1701114204/weather_background/drink-84533_1920_zsohp2.jpg";
                break;
            case "rain":
                result.iconUrl = "https://res.cloudinary.com/weather-station-viper/image/upload/v1698516317/weather_icons/cloudy_snowing_btnsjg.svg";
                result.backgroundUrl = "https://res.cloudinary.com/weather-station-viper/image/upload/v1701117551/corgi-4415649_1920_vmp4je.jpg";
                break;
            case "snow":
                result.iconUrl = "https://res.cloudinary.com/weather-station-viper/image/upload/v1698516317/weather_icons/cloudy_snowing_btnsjg.svg";
                result.backgroundUrl = "https://res.cloudinary.com/weather-station-viper/image/upload/v1700072486/549699_wxldp1.jpg";
                break;
            case "cold":
                result.iconUrl = "https://res.cloudinary.com/weather-station-viper/image/upload/v1698516376/weather_icons/thermostat2_qomkdz.svg";
                result.backgroundUrl = "https://res.cloudinary.com/weather-station-viper/image/upload/v1701115290/weather_background/soap-bubble-3187617_1280_lq7jmh.jpg";
                break;
             default : 
                result.iconUrl = "https://res.cloudinary.com/weather-station-viper/image/upload/v1698516376/weather_icons/thermostat2_qomkdz.svg";
                result.backgroundUrl = "https://res.cloudinary.com/weather-station-viper/image/upload/v1700072484/wp5821126-anime-hd-green-wallpapers_capydn.jpg";
            } 
        
        return result;
    }

    export {getTime, updateImageUrl}