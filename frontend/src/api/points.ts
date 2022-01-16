import { db } from "@/services/firebase";

class PointsApi {
    disasterId: string

    constructor(disasterId: string) {
        this.disasterId = disasterId
    }

    async getPoints() {
        const snapshot = await db.ref(`disasters/${this.disasterId}`).once('value')
        const info = snapshot.val()

        const features = []

        console.log(info)

        for (const [key, value] of Object.entries(info.responses)) {
            // @ts-ignore
            if (value.location?.lon != null && value.location?.lat != null) {
                 features.push({
                        type: "Feature",
                        properties: {},
                        geometry: {
                            type: "Point",
                            // @ts-ignore
                            coordinates: [value.location.lon, value.location.lat]
                        }
                    })
            }
        }

        return { type: "FeatureCollection", features }
    }
}

export { PointsApi }