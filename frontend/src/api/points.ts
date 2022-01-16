import { db } from "@/services/firebase";

class PointsApi {
    disasterId: string

    constructor(disasterId: string) {
        this.disasterId = disasterId
    }

    async getPoints() {
        const snapshot = await db.ref(`disasters`).once('value')
        const info = snapshot.val()

        const features = []

        console.log(info)

        for (const [k, disaster] of Object.entries(info)) {
            // @ts-ignore
            if (disaster.responses != null) {
                       // @ts-ignore
                for (const [key, value] of Object.entries(disaster.responses)) {
                    // @ts-ignore
                    if (value.location?.lon != null && value.location?.lat != null) {

                        features.push({
                            type: "Feature",
                            properties: {
                                // @ts-ignore
                                isOk: value.is_ok,
                                // @ts-ignore
                                message: value.message,
                                // @ts-ignore
                                phoneNumber: value.message,
                                // @ts-ignore
                                timestamp: value.timestamp
                            },
                            geometry: {
                                type: "Point",
                                // @ts-ignore
                                coordinates: [value.location.lon, value.location.lat]
                            }
                        })

                    }
                }
            }
        }

        return { type: "FeatureCollection", features }
    }
}

export { PointsApi }