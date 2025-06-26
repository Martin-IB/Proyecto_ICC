from fastapi import HTTPException
from models.sensores import Sensor
from repositories.sensores_repository import SensorRepository
from typing import List

class SensorService:
    def __init__(self, repository: SensorRepository):
        self.repository = repository

    def create_sensor(self, sensor: Sensor) -> int:
        return self.repository.create(sensor)

    def get_sensor(self, sensor_id: int) -> Sensor:
        sensor = self.repository.get_by_id(sensor_id)
        if not sensor:
            raise HTTPException(status_code=404, detail="Sensor no encontrado")
        return sensor

    def get_all_sensores(self) -> List[Sensor]:
        return self.repository.get_all()

    def update_sensor(self, sensor_id: int, sensor: Sensor) -> Sensor:
        success = self.repository.update(sensor_id, sensor)
        if not success:
            raise HTTPException(status_code=404, detail="Sensor no encontrado")
        return self.get_sensor(sensor_id)

    def delete_sensor(self, sensor_id: int) -> None:
        success = self.repository.delete(sensor_id)
        if not success:
            raise HTTPException(status_code=404, detail="Sensor no encontrado")

def get_sensor_service() -> SensorService:
    return SensorService(SensorRepository())
