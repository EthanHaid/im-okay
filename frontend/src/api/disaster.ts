import {axios} from "@/axios";

class DisasterAPI {
    disasterId: string
    phoneNumber: string
    lat: number | null = null
    lon: number | null = null

    constructor(disasterId: string | null, phoneNumber: string | null) {
        this.disasterId = disasterId!
        this.phoneNumber = phoneNumber!

    }

    updateLocation(pos: GeolocationPosition) {
        this.lat = pos.coords.latitude
        this.lon = pos.coords.longitude
    }

    async respondOk() {
        return this._respondToDisaster()
    }

    async respondHelp() {
        return this._respondToDisaster()
    }

    async _respondToDisaster() {
        return await axios.post(`/disasters/response/${1}`, {
            "is_ok": false,
            "message": "stub",
            "location": {
                lat: this.lat,
                lon: this.lon
            },
            "phone_number": this.phoneNumber
        })
    }
}

export { DisasterAPI }
