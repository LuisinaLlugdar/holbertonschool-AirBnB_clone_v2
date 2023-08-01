#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
<<<<<<< HEAD
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            result = {}
            for key, obj in FileStorage.__objects.items():
                if isinstance(obj, cls):
                    result[key] = obj
            return result
=======
        """Returns a dictionary of models currently in storage.
        If cls is not None, returns the list of objects of that type of class."""
        if cls is not None:
            return {key: value for key, value in FileStorage.__objects.items()
                    if isinstance(value, cls)}
        else:
            return FileStorage.__objects
>>>>>>> 370e01df993f8c808820546992f83c2cd2c08913

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
<<<<<<< HEAD
        """public instance method obj from __objects"""
        if obj is not None and \
                obj.__class__.__name__ + "." + obj.id in FileStorage.__objects:
            del FileStorage.__objects[obj.__class__.__name__ + "." + obj.id]
=======
        """delete obj from __objects if it's inside it"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            if key in FileStorage.__objects.keys():
                del FileStorage.__objects[key]
                self.save()
            else:
                pass
        else:
            pass
>>>>>>> 370e01df993f8c808820546992f83c2cd2c08913
