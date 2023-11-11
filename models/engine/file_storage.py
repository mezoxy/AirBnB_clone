#!/usr/bin/python3
"""The moduel: file_module"""
from json import loads, load, dumps, dump
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
        FileStorage:
                    A class that serializes instances to a JSON
                    file and deserializes JSON file to instances
        Public instance methods:
                    all(self): returns the dictionary __objects
                    new: sets in __objects the obj with key <obj class name>.id
                    save: serializes __objects to the JSON file
                    reload: deserializes the JSON file to __objects
                    (only if the JSON file
                    (__file_path) exists ; otherwise, do nothing.
    """
    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """
            returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
            new:
                sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
            save:
                serializes __objects to the JSON file (path: __file_path)
        """
        dic = {}
        for key, val in self.__objects.items():
            dic.update({key: val.to_dict()})
        with open(self.__file_path, "w") as w:
            w.write(dumps(dic))

    def reload(self):
        """
            reload:
                    deserializes the JSON file to __objects
                    (only if the JSON file (__file_path) exists
        """
        try:
            with open(self.__file_path, "r") as r:
                dic = load(r)
                new_dic = {}
                for key, val in dic.items():
                    new_dic[key] = eval(val["__class__"])(**val)
                self.__objects = new_dic
        except Exception as e:
            pass
