import {axios} from "@/axios";

class DisasterAPI {
    disasterId: string
    disaster_response_id: string
    lat: number | null = null
    lon: number | null = null

    constructor(disasterId: string | null, disaster_response_id: string | null) {
        this.disasterId = disasterId!
        this.disaster_response_id = disaster_response_id!

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
        return await axios.put(`/disasters/response/${this.disasterId}/${this.disaster_response_id}`, {
            "is_ok": String(false),
            "message": "stub",
            "location": {
                lat: this.lat,
                lon: this.lon
            },
            "disaster_response_id": this.disaster_response_id,
            "phone_number": "test"
        })
    }
}

export { DisasterAPI }
