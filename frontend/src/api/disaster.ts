import {axios} from "@/services/axios";

class DisasterAPI {
    disasterId: string
    disaster_response_id: string
    lat: number | null = null
    lon: number | null = null

    constructor(disasterId: any, disaster_response_id: any) {
        this.disasterId = disasterId == null ? "default" : String(disasterId);

        if (disaster_response_id == null) {
            this.disaster_response_id = "default"
            this._create_disaster_response(this.disasterId).then(id => this.disaster_response_id = id)
        } else {
            this.disaster_response_id = String(disaster_response_id)
        }
    }

    updateLocation(pos: GeolocationPosition) {
        this.lat = pos.coords.latitude
        this.lon = pos.coords.longitude
    }

    async respondOk(message: string) {
        return this._respondToDisaster("True", message)
    }

    async respondHelp(message: string) {
        return this._respondToDisaster("False", message)
    }

    async _respondToDisaster(isOk: string, message: string) {
        return await axios.put(`/disasters/response/${this.disasterId}/${this.disaster_response_id}`, {
            "is_ok": isOk,
            "message": message,
            "location": {
                lat: this.lat,
                lon: this.lon
            },
            "disaster_response_id": this.disaster_response_id,
            "phone_number": "test"
        })
    }

    async _create_disaster_response(id: string) {
        const data = (await axios.post(`/disasters/response/${id}`, {
            is_ok: "No Response",
            message: "",
            phone_number: "unknown"
        })).data

        return data.name
    }

    async getDisasters() {
        return await axios.get('/disasters/');
    }
}

export { DisasterAPI }
