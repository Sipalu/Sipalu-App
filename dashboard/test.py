
from cProfile import Profile
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from dashboard.models import BlogComment, Category, Order, Service, Worker

class LoginViewTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

    def test_login_view(self):
        # Test that the login view returns a 200 status code
        response = self.client.get(reverse('Login'))
        self.assertEqual(response.status_code, 200)
from django.test import TestCase
from django.contrib.auth.models import User
from .models import OrderItem, Profile, ShippingAddress

class ProfileModelTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
            first_name='Test',
            last_name='User',
            email='test@example.com'
        )
        # Add additional setup code as needed

    def test_profile_model(self):
        # Test creating a Profile instance
        profile = Profile(
            user=self.user,
            firstname='Test',
            lastname='User',
            email='test@example.com',
            phone='1234567890',
            district='Test District',
            city='Test City'
        )
        profile.save()
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.firstname, 'Test')
        self.assertEqual(profile.lastname, 'User')
        self.assertEqual(profile.email, 'test@example.com')
        self.assertEqual(profile.phone, '1234567890')
        self.assertEqual(profile.district, 'Test District')
        self.assertEqual(profile.city, 'Test City')
        # Test the str method of Profile
        self.assertEqual(str(profile), 'Test User')



class CategoryModelTestCase(TestCase):
    def setUp(self):
        # Create a Category object for testing
        self.category = Category.objects.create(
            name='Test Category',
            image='static/category/images/testcategory.jpg',
            description='This is a test category'
        )

    def test_category_str(self):
         # Test creating a Category instance
        self.assertEqual(self.category.name, 'Test Category')
        self.assertEqual(self.category.image.name, 'static/category/images/testcategory.jpg')
        self.assertEqual(self.category.description, 'This is a test category')
        # Test that the __str__ method of the Category model returns the expected string
        self.assertEqual(str(self.category), 'Test Category')


class ServiceModelTestCase(TestCase):
    def setUp(self):
        # Create a worker for testing
        self.worker = Worker.objects.create(
            worker_name='Test',
            phone='1234567890',
            address='address1'
        )
        # Create a category for testing
        self.category = Category.objects.create(
            name='Test Category'
        )
        # Add additional setup code as needed

    def test_service_model(self):
        # Test creating a new service
        service = Service.objects.create(
            service_name='Test Service',
            worker=self.worker,
            category=self.category,
            price=100.0,
            service_details='This is a test service'
        )
        # Check if the service was created correctly
        self.assertEqual(service.service_name, 'Test Service')
        self.assertEqual(service.worker, self.worker)
        self.assertEqual(service.category, self.category)
        self.assertEqual(service.price, 100.0)
        self.assertEqual(service.service_details, 'This is a test service')


class OrderModelTestCase(TestCase):
    def setUp(self):
        
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
            first_name='Test',
            last_name='User',
            email='test@example.com'
        )
        # Add additional setup code as needed

    def test_order_model(self):
        # Test creating an Order instance
        order = Order.objects.create(
            customer=self.user,
            transaction_id='12345',
            status='booked'
        )
        self.assertEqual(order.customer, self.user)
        self.assertEqual(order.transaction_id, '12345')
        self.assertEqual(order.status, 'booked')

        # Test the str method of the Order model
        self.assertEqual(str(order), '4')

class BlogCommentModelTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
            first_name='Test',
            last_name='User',
            email='test@example.com'
        )
        # Create a service for testing
        self.service = Service.objects.create(
            category=Category.objects.create(name='Test Category'),
            service_name='Test Service',
            title='Test Title',
            price=100,
            service_details='Test service details',
            worker=Worker.objects.create(worker_name='Test Worker', phone = '1234567890'),
            status='available'
        )
        # Add additional setup code as needed

    def test_blog_comment_model(self):
        # Test creating a BlogComment instance
        comment = BlogComment.objects.create(
            user=self.user,
            comment_post='Test comment',
            service=self.service
        )
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.comment_post, 'Test comment')
        self.assertEqual(comment.service, self.service)
        # Test the str method of BlogComment
        self.assertEqual(str(comment), 'Test comme...by testuser')


class ShippingAddressModelTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
            first_name='Test',
            last_name='User',
            email='test@example.com'
        )
        # Add additional setup code as needed

    def test_shipping_address_model(self):
        # Test creating a ShippingAddress instance
        shipping_address = ShippingAddress.objects.create(
            customer=self.user,
            address='123 Main St',
            city='New York',
            state='NY',
            zipcode='10001'
        )
        self.assertEqual(shipping_address.customer, self.user)
        self.assertEqual(shipping_address.address, '123 Main St')
        self.assertEqual(shipping_address.city, 'New York')
        self.assertEqual(shipping_address.state, 'NY')
        self.assertEqual(shipping_address.zipcode, '10001')
        # Test the str method of ShippingAddress
        self.assertEqual(str(shipping_address), '123 Main St')


class OrderItemModelTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
        username='testuser',
        password='testpass',
        first_name='Test',
        last_name='User',
        email='test@example.com'
        )
        # Create an order for testing
        self.order = Order.objects.create(
        customer=self.user,
        transaction_id='12345',
        status='booked'
        )
        # Create a service for testing
        self.service = Service.objects.create(
        category=Category.objects.create(name='Test Category'),
        service_name='Test Service',
        title='Test Title',
        price=100,
        service_details='Test service details',
        worker=Worker.objects.create(worker_name='Test Worker', phone = '1234567890'),
        status='available'
        )
        # Add additional setup code as needed
    def test_order_item_model(self):
        # Test creating an OrderItem instance
        order_item = OrderItem.objects.create(
            service=self.service,
            order=self.order,
            quantity=1,
        )
        self.assertEqual(order_item.service, self.service)
        self.assertEqual(order_item.order, self.order)
        self.assertEqual(order_item.quantity, 1)
        # Test the str method of OrderItem
        self.assertEqual(str(order_item), '1')


class CheckoutViewTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
            first_name='Test',
            last_name='User',
            email='test@example.com'
        )
        # Create an Order instance for testing
        self.order = Order.objects.create(
            customer=self.user,
            transaction_id='12345',
            status='approved'
        )
        # Add additional setup code as needed

    def test_checkout_view(self):
        # Test accessing the checkout view with a valid Order instance
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/checkout.html')

        # Test accessing the checkout view with an invalid Order instance
        self.order.delete()
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)



